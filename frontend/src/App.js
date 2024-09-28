// src/App.js
import React, { useState, useEffect } from 'react';
import {
  BrowserRouter as Router,
  Routes,
  Route,
  useNavigate,
  useLocation,
} from 'react-router-dom';
import { Download, MessageSquare, Search, Youtube } from 'lucide-react';
import './App.css'; // Ensure Tailwind CSS is imported here

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<InitialPage />} />
        <Route path="/loading" element={<LoadingPage />} />
        <Route path="/dashboard" element={<StudentDashboard />} />
        <Route path="/quiz" element={<QuizPage />} />
      </Routes>
    </Router>
  );
}

export default App;

// ======================== Initial Upload Page ========================

function InitialPage() {
  const navigate = useNavigate();
  const [file, setFile] = useState(null);
  const [courseNumber, setCourseNumber] = useState('');
  const [error, setError] = useState('');

  // Handle file selection
  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  // Handle course number input
  const handleCourseNumberChange = (e) => {
    setCourseNumber(e.target.value);
  };

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();

    // Validate inputs
    if (!file || !courseNumber) {
      setError('Please upload a file and enter a course number.');
      return;
    }
    setError('');

    // Prepare form data
    const formData = new FormData();
    formData.append('file', file);
    formData.append('course', courseNumber);

    try {
      // Send POST request to /get_pdf
      const response = await fetch('/get_pdf', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        throw new Error('Failed to upload file.');
      }

      const data = await response.json();
      const uuid = data.uuid;

      // Navigate to Loading Page with uuid and courseNumber
      navigate('/loading', { state: { uuid, courseNumber } });
    } catch (err) {
      setError(err.message || 'Something went wrong.');
    }
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold mb-6">Welcome to the Student Learning Platform</h1>
      <form onSubmit={handleSubmit} className="space-y-4">
        {/* File Upload */}
        <div>
          <label className="block text-lg font-medium mb-2">Upload PDF:</label>
          <input
            type="file"
            accept=".pdf"
            onChange={handleFileChange}
            className="border p-2 w-full"
            required
          />
        </div>

        {/* Course Number Input */}
        <div>
          <label className="block text-lg font-medium mb-2">Course Number:</label>
          <input
            type="text"
            value={courseNumber}
            onChange={handleCourseNumberChange}
            placeholder="e.g., CS101"
            className="border p-2 w-full"
            required
          />
        </div>

        {/* Error Message */}
        {error && <p className="text-red-500">{error}</p>}

        {/* Submit Button */}
        <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded">
          Submit
        </button>
      </form>
    </div>
  );
}

// ======================== Loading Page ========================

function LoadingPage() {
  const navigate = useNavigate();
  const location = useLocation();
  const { uuid, courseNumber } = location.state || {};

  const [status, setStatus] = useState('processing');
  const [data, setData] = useState(null);
  const [error, setError] = useState('');

  // Polling function to check status every 2 seconds
  useEffect(() => {
    if (!uuid) {
      setError('No file ID provided.');
      return;
    }

    const interval = setInterval(async () => {
      try {
        const response = await fetch(`/status?file_id=${uuid}`);
        if (!response.ok) {
          throw new Error('Failed to fetch status.');
        }

        const result = await response.json();
        if (result.status === 'done') {
          setStatus('done');
          setData(result.results);
          clearInterval(interval);
          // Navigate to Student Dashboard with received data
          navigate('/dashboard', { state: { data: result.results, uuid, courseNumber } });
        } else {
          setStatus(result.status);
        }
      } catch (err) {
        setError(err.message || 'Something went wrong.');
        clearInterval(interval);
      }
    }, 2000); // 2 seconds interval

    return () => clearInterval(interval);
  }, [uuid, navigate, courseNumber]);

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Processing Your File...</h1>
      {error ? (
        <p className="text-red-500">{error}</p>
      ) : (
        <div className="flex items-center space-x-2">
          {/* Loading Spinner */}
          <div className="animate-spin rounded-full h-8 w-8 border-t-2 border-b-2 border-blue-500"></div>
          <span>Loading...</span>
        </div>
      )}
    </div>
  );
}

// ======================== Student Dashboard ========================

function StudentDashboard() {
  const location = useLocation();
  const { data, uuid, courseNumber } = location.state || {};
  const navigate = useNavigate();

  const [chatMessages, setChatMessages] = useState([]);
  const [chatInput, setChatInput] = useState('');
  const [activeTab, setActiveTab] = useState('chapter1');
  const [searchTerm, setSearchTerm] = useState('');
  const [filteredGlossary, setFilteredGlossary] = useState([]);
  const [textbookLinks, setTextbookLinks] = useState({ chapter1: [], chapter2: [], chapter3: [] });

  // Glossary Terms (can be fetched from backend if dynamic)
  const glossaryTerms = [
    { term: 'React', definition: 'A JavaScript library for building user interfaces.' },
    { term: 'Component', definition: 'Reusable pieces of UI in React.' },
    { term: 'State', definition: 'An object that determines how a component renders and behaves.' },
    // Add more terms as needed
  ];

  // Handle chat form submission
  const handleChatSubmit = async (e) => {
    e.preventDefault();
    if (chatInput.trim()) {
      // Add user message
      setChatMessages((prev) => [...prev, { text: chatInput, sender: 'user' }]);

      try {
        // Send POST request to /get_response
        const response = await fetch('/get_response', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ question: chatInput, uuid }),
        });

        if (!response.ok) {
          throw new Error('Failed to get response.');
        }

        const resData = await response.json();
        const botAnswer = resData.answer;

        // Add bot response
        setChatMessages((prev) => [...prev, { text: botAnswer, sender: 'bot' }]);
        setChatInput('');
      } catch (err) {
        setChatMessages((prev) => [...prev, { text: 'Error getting response.', sender: 'bot' }]);
        setChatInput('');
      }
    }
  };

  // Handle glossary search
  const handleSearch = (e) => {
    const value = e.target.value;
    setSearchTerm(value);
    if (value.trim() === '') {
      setFilteredGlossary(glossaryTerms);
    } else {
      const filtered = glossaryTerms.filter((term) =>
        term.term.toLowerCase().includes(value.toLowerCase())
      );
      setFilteredGlossary(filtered);
    }
  };

  // Initialize glossary with all terms
  useEffect(() => {
    setFilteredGlossary(glossaryTerms);
  }, []);

  // Fetch textbook links on component mount
  useEffect(() => {
    const fetchTextbookLinks = async () => {
      try {
        const response = await fetch('/get_textbook', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ course: courseNumber, uuid }),
        });

        if (!response.ok) {
          throw new Error('Failed to fetch textbook links.');
        }

        const resData = await response.json();
        // Assuming resData.links is an object like { chapter1: [url1, url2], chapter2: [...], chapter3: [...] }
        setTextbookLinks(resData.links);
      } catch (err) {
        // Handle error (optional)
        console.error(err);
      }
    };

    fetchTextbookLinks();
  }, [uuid, courseNumber]);

  // Handle "Take Quiz" button click
  const handleTakeQuiz = () => {
    navigate('/quiz', { state: { uuid } });
  };

  // Redirect if no data is available
  if (!data) {
    return (
      <div className="container mx-auto p-4">
        <p>No data available. Please go back and upload a file.</p>
      </div>
    );
  }

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-6">Student Learning Dashboard</h1>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {/* Main Content Area */}
        <div className="md:col-span-2 space-y-6">
          {/* PDF Viewer */}
          <div className="border rounded-lg p-4">
            <h2 className="text-xl font-semibold mb-2">PDF Viewer</h2>
            <div className="bg-gray-200 h-96 flex items-center justify-center">
              {/* Integrate a PDF viewer library here if desired */}
              <a href={data.pdf} target="_blank" rel="noopener noreferrer">
                View PDF
              </a>
            </div>
            <div className="mt-4 flex space-x-2">
              <a
                href={data.pdf}
                download
                className="bg-blue-500 text-white px-4 py-2 rounded flex items-center"
              >
                <Download className="mr-2 h-4 w-4" /> Download PDF
              </a>
              <button
                className="border border-gray-300 px-4 py-2 rounded"
                onClick={handleTakeQuiz}
              >
                Take Quiz
              </button>
            </div>
          </div>

          {/* Related Videos */}
          <div className="border rounded-lg p-4">
            <h2 className="text-xl font-semibold mb-2">Related Videos</h2>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              {data.videos &&
                Object.keys(data.videos).map((videoKey) => (
                  <div
                    key={videoKey}
                    className="bg-gray-200 h-40 flex flex-col items-center justify-center p-2"
                  >
                    <Youtube className="h-8 w-8 mb-2" />
                    <a
                      href={data.videos[videoKey].url}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="text-blue-500 underline"
                    >
                      {data.videos[videoKey].title}
                    </a>
                  </div>
                ))}
            </div>
          </div>
        </div>

        {/* Sidebar */}
        <div className="space-y-6">
          {/* Glossary */}
          <div className="border rounded-lg p-4">
            <h2 className="text-xl font-semibold mb-2">Glossary</h2>
            <div className="flex mb-2">
              <input
                type="text"
                placeholder="Search terms..."
                value={searchTerm}
                onChange={handleSearch}
                className="flex-grow border rounded-l px-2 py-1"
              />
              <button className="bg-gray-200 px-2 py-1 rounded-r">
                <Search className="h-4 w-4" />
              </button>
            </div>
            <div className="h-40 overflow-y-auto">
              <ul className="space-y-2">
                {filteredGlossary.map((item) => (
                  <li key={item.term} className="flex justify-between">
                    <span className="font-medium">{item.term}</span>
                    <span className="text-gray-500">{item.definition}</span>
                  </li>
                ))}
              </ul>
            </div>
          </div>

          {/* Chat Interface */}
          <div className="border rounded-lg p-4">
            <h2 className="text-xl font-semibold mb-2">Ask a Question</h2>
            <div className="h-40 mb-2 overflow-y-auto">
              {chatMessages.map((msg, index) => (
                <div
                  key={index}
                  className={`mb-2 ${
                    msg.sender === 'user' ? 'text-right' : 'text-left'
                  }`}
                >
                  <span
                    className={`inline-block p-2 rounded-lg ${
                      msg.sender === 'user' ? 'bg-blue-100' : 'bg-gray-100'
                    }`}
                  >
                    {msg.text}
                  </span>
                </div>
              ))}
            </div>
            <form onSubmit={handleChatSubmit} className="flex">
              <input
                type="text"
                placeholder="Type your question..."
                value={chatInput}
                onChange={(e) => setChatInput(e.target.value)}
                className="flex-grow border rounded-l px-2 py-1"
              />
              <button type="submit" className="bg-gray-200 px-2 py-1 rounded-r">
                <MessageSquare className="h-4 w-4" />
              </button>
            </form>
          </div>

          {/* Relevant Textbook Pages */}
          <div className="border rounded-lg p-4">
            <h2 className="text-xl font-semibold mb-2">Relevant Textbook Pages</h2>
            <div className="mb-2">
              <button
                onClick={() => setActiveTab('chapter1')}
                className={`px-2 py-1 mr-2 ${
                  activeTab === 'chapter1' ? 'bg-gray-200' : ''
                }`}
              >
                Chapter 1
              </button>
              <button
                onClick={() => setActiveTab('chapter2')}
                className={`px-2 py-1 mr-2 ${
                  activeTab === 'chapter2' ? 'bg-gray-200' : ''
                }`}
              >
                Chapter 2
              </button>
              <button
                onClick={() => setActiveTab('chapter3')}
                className={`px-2 py-1 ${
                  activeTab === 'chapter3' ? 'bg-gray-200' : ''
                }`}
              >
                Chapter 3
              </button>
            </div>
            <div>
              {activeTab === 'chapter1' && (
                <ul className="list-disc list-inside">
                  {textbookLinks.chapter1 &&
                    textbookLinks.chapter1.map((link, idx) => (
                      <li key={idx}>
                        <a
                          href={link}
                          target="_blank"
                          rel="noopener noreferrer"
                          className="text-blue-500 underline"
                        >
                          {link}
                        </a>
                      </li>
                    ))}
                </ul>
              )}
              {activeTab === 'chapter2' && (
                <ul className="list-disc list-inside">
                  {textbookLinks.chapter2 &&
                    textbookLinks.chapter2.map((link, idx) => (
                      <li key={idx}>
                        <a
                          href={link}
                          target="_blank"
                          rel="noopener noreferrer"
                          className="text-blue-500 underline"
                        >
                          {link}
                        </a>
                      </li>
                    ))}
                </ul>
              )}
              {activeTab === 'chapter3' && (
                <ul className="list-disc list-inside">
                  {textbookLinks.chapter3 &&
                    textbookLinks.chapter3.map((link, idx) => (
                      <li key={idx}>
                        <a
                          href={link}
                          target="_blank"
                          rel="noopener noreferrer"
                          className="text-blue-500 underline"
                        >
                          {link}
                        </a>
                      </li>
                    ))}
                </ul>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

// ======================== Quiz Page ========================

function QuizPage() {
  const location = useLocation();
  const { uuid } = location.state || {};
  const navigate = useNavigate();

  const [quizzes, setQuizzes] = useState(null);
  const [error, setError] = useState('');
  const [selectedAnswers, setSelectedAnswers] = useState({});
  const [score, setScore] = useState(null);

  // Fetch quizzes on component mount
  useEffect(() => {
    const fetchQuizzes = async () => {
      try {
        const response = await fetch('/get_quizzes', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ uuid }),
        });

        if (!response.ok) {
          throw new Error('Failed to fetch quizzes.');
        }

        const data = await response.json();
        setQuizzes(data);
      } catch (err) {
        setError(err.message || 'Something went wrong.');
      }
    };

    fetchQuizzes();
  }, [uuid]);

  // Handle multiple choice answer selection
  const handleMultipleChoiceChange = (qKey, answer) => {
    setSelectedAnswers((prev) => ({
      ...prev,
      [qKey]: answer,
    }));
  };

  // Handle quiz submission
  const handleSubmit = (e) => {
    e.preventDefault();
    if (!quizzes) return;

    let calculatedScore = 0;
    const multipleChoice = quizzes.multiple_choice;
    const freeResponse = quizzes.free_response;

    // Check multiple choice answers
    for (const qKey in multipleChoice) {
      if (selectedAnswers[qKey] === multipleChoice[qKey].correct) {
        calculatedScore += 1;
      }
    }

    // For free response questions, grading would typically be manual or handled by the backend
    // Here, we'll only count multiple choice questions

    setScore(calculatedScore);
  };

  // Redirect if no uuid is provided
  if (!uuid) {
    return (
      <div className="container mx-auto p-4">
        <p>No quiz data available. Please go back and complete the process.</p>
      </div>
    );
  }

  // Display error message if any
  if (error) {
    return (
      <div className="container mx-auto p-4">
        <p className="text-red-500">{error}</p>
      </div>
    );
  }

  // Display loading indicator while fetching quizzes
  if (!quizzes) {
    return (
      <div className="container mx-auto p-4">
        <h1 className="text-2xl font-bold mb-4">Loading Quizzes...</h1>
        <div className="flex items-center space-x-2">
          <div className="animate-spin rounded-full h-8 w-8 border-t-2 border-b-2 border-blue-500"></div>
          <span>Loading...</span>
        </div>
      </div>
    );
  }

  // Display score after submission
  if (score !== null) {
    return (
      <div className="container mx-auto p-4">
        <h1 className="text-2xl font-bold mb-4">Quiz Completed!</h1>
        <p>Your Score: {score} / {Object.keys(quizzes.multiple_choice).length}</p>
        <button
          onClick={() => navigate('/')}
          className="mt-4 bg-blue-500 text-white px-4 py-2 rounded"
        >
          Go Home
        </button>
      </div>
    );
  }

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-6">Quiz</h1>
      <form onSubmit={handleSubmit} className="space-y-6">
        {/* Multiple Choice Questions */}
        <div>
          <h2 className="text-xl font-semibold mb-2">Multiple Choice Questions</h2>
          {Object.keys(quizzes.multiple_choice).map((qKey, index) => {
            const question = quizzes.multiple_choice[qKey].question;
            const answers = quizzes.multiple_choice[qKey].answers;
            return (
              <div key={qKey} className="mb-4">
                <p className="font-medium">{index + 1}. {question}</p>
                <div className="ml-4">
                  {answers.map((ans, idx) => (
                    <label key={idx} className="block">
                      <input
                        type="radio"
                        name={qKey}
                        value={ans}
                        checked={selectedAnswers[qKey] === ans}
                        onChange={() => handleMultipleChoiceChange(qKey, ans)}
                        className="mr-2"
                      />
                      {ans}
                    </label>
                  ))}
                </div>
              </div>
            );
          })}
        </div>

        {/* Free Response Questions */}
        <div>
          <h2 className="text-xl font-semibold mb-2">Free Response Questions</h2>
          {Object.keys(quizzes.free_response).map((qKey, index) => {
            const question = quizzes.free_response[qKey].question;
            return (
              <div key={qKey} className="mb-4">
                <p className="font-medium">{index + 1}. {question}</p>
                <textarea
                  className="border p-2 w-full"
                  rows="4"
                  placeholder="Your answer..."
                ></textarea>
              </div>
            );
          })}
        </div>

        {/* Submit Button */}
        <button type="submit" className="bg-green-500 text-white px-4 py-2 rounded">
          Submit Quiz
        </button>
      </form>
    </div>
  );
}

