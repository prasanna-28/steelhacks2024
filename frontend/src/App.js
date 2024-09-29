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

    try {
      // Send POST request to /get_pdf
      const response = await fetch(`http://127.0.0.1:5000/get_pdf?course=${encodeURIComponent(courseNumber)}`, {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || 'Failed to upload file.');
      }

      const data = await response.json();
      const file_id = data.file_id;

      // Navigate to Loading Page with file_id and courseNumber
      navigate('/loading', { state: { file_id, courseNumber } });
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
  const { file_id, courseNumber } = location.state || {};

  const [status, setStatus] = useState('Processing');
  const [error, setError] = useState('');

  // Polling function to check status every 2 seconds
  useEffect(() => {
    if (!file_id) {
      setError('No file ID provided.');
      return;
    }

    const interval = setInterval(async () => {
      try {
        const response = await fetch(`http://127.0.0.1:5000/status?file_id=${file_id}`);
        if (!response.ok) {
          const errorData = await response.json();
          throw new Error(errorData.error || 'Failed to fetch status.');
        }

        const result = await response.json();
        if (result.status === 'done') {
          setStatus('done');
          clearInterval(interval);
          // Navigate to Student Dashboard with received data
          navigate('/dashboard', { state: { data: result.result, file_id, courseNumber } });
        } else {
          setStatus(result.status);
        }
      } catch (err) {
        setError(err.message || 'Something went wrong.');
        clearInterval(interval);
      }
    }, 2000); // 2 seconds interval

    return () => clearInterval(interval);
  }, [file_id, navigate, courseNumber]);

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Processing Your File...</h1>
      {error ? (
        <p className="text-red-500">{error}</p>
      ) : (
        <div className="flex items-center space-x-2">
          {/* Loading Spinner */}
          <div className="animate-spin rounded-full h-8 w-8 border-t-2 border-b-2 border-blue-500"></div>
          <span>{status}...</span>
        </div>
      )}
    </div>
  );
}

// ======================== Student Dashboard ========================

function StudentDashboard() {
  const location = useLocation();
  const { data, file_id, courseNumber } = location.state || {};
  const navigate = useNavigate();

  const [chatMessages, setChatMessages] = useState([]);
  const [chatInput, setChatInput] = useState('');
  const [searchTerm, setSearchTerm] = useState('');
  const [filteredGlossary, setFilteredGlossary] = useState([]);
  const [textbookLink, setTextbookLink] = useState('');
  const [glossaryTerms, setGlossaryTerms] = useState([]);
  const [videos, setVideos] = useState([]);
  const [summary, setSummary] = useState('');

  // Extract data from the response
  useEffect(() => {
    if (data) {
      const pdfUrl = data.filepath;
      const glossary = data.glossary;
      const summaryText = data.summary;
      const link = data.link;
      const videoData = data.videos;

      setTextbookLink(link);
      setSummary(summaryText);
      setVideos(videoData || []);

      // Parse glossary object
      if (glossary) {
        const terms = Object.keys(glossary).map((key) => ({
          term: key,
          definition: glossary[key],
        }));
        setGlossaryTerms(terms);
        setFilteredGlossary(terms);
      }

      // Set PDF URL (if needed elsewhere)
    }
  }, [data]);

  // Handle chat form submission
  const handleChatSubmit = async (e) => {
    e.preventDefault();
    if (chatInput.trim()) {
      // Add user message
      setChatMessages((prev) => [...prev, { text: chatInput, sender: 'user' }]);

      try {
        // Send POST request to /get_response
        const response = await fetch('http://127.0.0.1:5000/get_response', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ message: chatInput, uuid: file_id }),
        });

        if (!response.ok) {
          const errorData = await response.text();
          throw new Error(errorData || 'Failed to get response.');
        }

        const botAnswer = await response.text();

        // Add bot response
        setChatMessages((prev) => [...prev, { text: botAnswer, sender: 'bot' }]);
        setChatInput('');
      } catch (err) {
        setChatMessages((prev) => [
          ...prev,
          { text: err.message || 'Error getting response.', sender: 'bot' },
        ]);
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

  // Handle "Take Quiz" button click
  const handleTakeQuiz = () => {
    navigate('/quiz', { state: { uuid: file_id } });
  };

  // Redirect if no data is available
  if (!data) {
    return (
      <div className="container mx-auto p-4">
        <p>No data available. Please go back and upload a file.</p>
      </div>
    );
  }

  const pdfURL = "http://127.0.0.1:5000/cdn/pdf/" + data.filepath + "#zoom=90";

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-6">Student Learning Dashboard</h1>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {/* Main Content Area */}
        <div className="md:col-span-2 space-y-6">
          {/* PDF Viewer */}
          <div className="border rounded-lg p-4">
            <h2 className="text-xl font-semibold mb-2">PDF Viewer</h2>
            <div className="bg-gray-200 h-[583px] flex items-center justify-center">
              {/* Integrate a PDF viewer library here if desired */}
              <iframe
                src={pdfURL}
                width="100%"
                height="100%"
                frameBorder="0"
                ></iframe>
            </div>
            <div className="mt-4 flex space-x-2">
              <a
                href={pdfURL}
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
              {videos && videos.length > 0 ? (
                videos.map((videoList, idx) =>
                  videoList.map((video, index) => (
                    <div
                      key={`${idx}-${index}`}
                      className="bg-gray-200 h-40 flex flex-col items-center justify-center p-2"
                    >
                    <iframe
                        width="100%"
                        height="200"
                        src={`https://www.youtube.com/embed/${video.videoId}`}
                        frameBorder="0"
                        allowFullScreen>
                    </iframe>
                    </div>
                  ))
                )
              ) : (
                <p>No related videos found.</p>
              )}
            </div>
          </div>

          {/* Summary */}
          <div className="border rounded-lg p-4">
            <h2 className="text-xl font-semibold mb-2">Summary</h2>
            <p>{summary}</p>
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
                {filteredGlossary.length > 0 ? (
                  filteredGlossary.map((item, idx) => (
                    <li key={idx}>
                      <span className="font-medium">{item.term}:</span>{' '}
                      <span className="text-gray-500">{item.definition}</span>
                    </li>
                  ))
                ) : (
                  <p>No terms found.</p>
                )}
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

          {/* Relevant Textbook Page */}
          <div className="border rounded-lg p-4">
            <h2 className="text-xl font-semibold mb-2">Relevant Textbook Page</h2>
            {textbookLink ? (
              <ul className="list-disc list-inside">
                <li>
                  <a
                    href={textbookLink}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-blue-500 underline"
                  >
                    {textbookLink}
                  </a>
                </li>
              </ul>
            ) : (
              <p>No textbook link available.</p>
            )}
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
        const response = await fetch('http://127.0.0.1:5000/get_quizzes', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ uuid }),
        });

        if (!response.ok) {
          const errorData = await response.json();
          throw new Error(errorData.error || 'Failed to fetch quizzes.');
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

    // Check multiple choice answers
    for (const qKey in quizzes) {
      const questionData = quizzes[qKey];
      if (selectedAnswers[qKey] === questionData.correct_answer) {
        calculatedScore += 1;
      }
    }

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
        <p>
          Your Score: {score} / {Object.keys(quizzes).length}
        </p>
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
          {Object.keys(quizzes).map((qKey, index) => {
            const questionData = quizzes[qKey];
            const question = questionData.question;
            const answers = [
              ...questionData.wrong_answers,
              questionData.correct_answer,
            ].sort();

            return (
              <div key={qKey} className="mb-4">
                <p className="font-medium">
                  {index + 1}. {question}
                </p>
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

        {/* Submit Button */}
        <button type="submit" className="bg-green-500 text-white px-4 py-2 rounded">
          Submit Quiz
        </button>
      </form>
    </div>
  );
}
