// src/App.js
import React, { useState, useEffect, useRef } from 'react';
import {
  BrowserRouter as Router,
  Routes,
  Route,
  useNavigate,
  useLocation,
} from 'react-router-dom';
import { Download, MessageSquare, Search, Upload } from 'lucide-react';
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

  const handleFileChange = (e) => {
    if (e.target.files) {
      setFile(e.target.files[0]);
    }
  };

  const handleCourseNumberChange = (e) => {
    setCourseNumber(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!file || !courseNumber) {
      setError('Please upload a file and enter a course number.');
      return;
    }
    setError('');

    // Navigate to Loading Page immediately, passing file and courseNumber
    navigate('/loading', { state: { file, courseNumber } });
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-100 to-indigo-100 flex items-center justify-center p-4">
      <div className="bg-white rounded-lg shadow-xl p-8 max-w-md w-full">
        <h1 className="text-3xl font-bold mb-6 text-center text-indigo-700">
          Student Learning Platform
        </h1>
        <form onSubmit={handleSubmit} className="space-y-6">
          {/* File Upload */}
          <div className="space-y-2">
            <label className="block text-sm font-medium text-gray-700">
              Upload PDF
            </label>
            <div className="flex items-center justify-center w-full">
              <label
                htmlFor="dropzone-file"
                className="flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 hover:bg-gray-100"
              >
                <div className="flex flex-col items-center justify-center pt-5 pb-6">
                  <Upload className="w-10 h-10 mb-3 text-gray-400" />
                  <p className="mb-2 text-sm text-gray-500">
                    <span className="font-semibold">Click to upload</span> or
                    drag and drop
                  </p>
                  <p className="text-xs text-gray-500">PDF (MAX. 10MB)</p>
                </div>
                <input
                  id="dropzone-file"
                  type="file"
                  className="hidden"
                  accept=".pdf"
                  onChange={handleFileChange}
                  required
                />
              </label>
            </div>
            {file && (
              <p className="text-sm text-gray-500">Selected file: {file.name}</p>
            )}
          </div>

          {/* Course Number Input */}
          <div className="space-y-2">
            <label
              htmlFor="courseNumber"
              className="block text-sm font-medium text-gray-700"
            >
              Course Number
            </label>
            <input
              type="text"
              id="courseNumber"
              value={courseNumber}
              onChange={handleCourseNumberChange}
              placeholder="e.g., CS101"
              className="block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
              required
            />
          </div>

          {/* Error Message */}
          {error && <p className="text-red-500 text-sm">{error}</p>}

          {/* Submit Button */}
          <button
            type="submit"
            className="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
          >
            Submit
          </button>
        </form>
      </div>
    </div>
  );
}

// ======================== Loading Page ========================

function LoadingPage() {
  const navigate = useNavigate();
  const location = useLocation();
  const { file, courseNumber } = location.state || {};

  const [status, setStatus] = useState('Uploading');
  const [error, setError] = useState('');
  const [fileId, setFileId] = useState(null);

  // Ref to prevent multiple uploads
  const didUpload = useRef(false);

  useEffect(() => {
    if (!file || !courseNumber) {
      setError('File or course number is missing.');
      return;
    }

    if (didUpload.current) {
      return;
    }
    didUpload.current = true;

    const uploadFile = async () => {
      setStatus('Uploading');

      const formData = new FormData();
      formData.append('file', file);

      try {
        // Send POST request to /get_pdf
        const response = await fetch(
          `http://127.0.0.1:5000/get_pdf?course=${encodeURIComponent(
            courseNumber
          )}`,
          {
            method: 'POST',
            body: formData,
            credentials: 'include',

          }
        );

        if (!response.ok) {
          const errorData = await response.json();
          throw new Error(errorData.error || 'Failed to upload file.');
        }

        const data = await response.json();
        const file_id = data.file_id;
        setFileId(file_id);

        // Start polling for status
        pollStatus(file_id);
      } catch (err) {
        setError(err.message || 'Something went wrong during upload.');
      }
    };

    const pollStatus = (file_id) => {
      setStatus('Processing');
      const interval = setInterval(async () => {
        try {
          const response = await fetch(
            `http://127.0.0.1:5000/status?file_id=${file_id}`,
            {
                method: "GET"
            }
          );
          if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || 'Failed to fetch status.');
          }

          const result = await response.json();
          if (result.status === 'done') {
            setStatus('Completed');
            clearInterval(interval);
            // Navigate to Student Dashboard with received data
            navigate('/dashboard', {
              state: { data: result.result, file_id, courseNumber },
            });
          } else {
            setStatus(
              result.status.charAt(0).toUpperCase() + result.status.slice(1)
            );
          }
        } catch (err) {
          setError(err.message || 'Something went wrong during processing.');
          clearInterval(interval);
        }
      }, 2000); // 2 seconds interval
    };

    uploadFile();
  }, [file, courseNumber, navigate]);

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-100 to-indigo-100 flex flex-col items-center justify-center p-4">
      <div className="bg-white rounded-lg shadow-xl p-8 max-w-lg w-full text-center">
        <h1 className="text-2xl font-bold mb-4 text-indigo-700">
          {status} Your File...
        </h1>
        {error ? (
          <p className="text-red-500">{error}</p>
        ) : (
          <div className="flex flex-col items-center space-y-4">
            {/* Loading Spinner */}
            <div className="animate-spin rounded-full h-16 w-16 border-t-4 border-b-4 border-indigo-600"></div>
            <span className="text-lg font-medium text-gray-700">
              {status}...
            </span>
            <p className="text-gray-500">
              This may take a few moments. Please wait.
            </p>
          </div>
        )}
      </div>
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
  const [activeTab, setActiveTab] = useState('PDF');

  // Extract data from the response
  useEffect(() => {
    if (data) {
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
        setChatMessages((prev) => [
          ...prev,
          { text: botAnswer, sender: 'bot' },
        ]);
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

  const pdfURL =
    'http://127.0.0.1:5000/cdn/pdf/' + data.filepath + '#zoom=90';

  return (
    <div className="min-h-screen bg-gray-50 p-4">
      <h1 className="text-3xl font-bold mb-6 text-indigo-700 text-center">
        Student Learning Dashboard
      </h1>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {/* Main Content Area */}
        <div className="md:col-span-2 space-y-6">
          {/* Tabbed Viewer */}
          <div className="bg-white border rounded-lg p-4 shadow">
            {/* Tabs */}
            <div className="flex mb-4 border-b">
              <button
                className={`mr-4 pb-2 ${
                  activeTab === 'PDF'
                    ? 'border-b-2 border-indigo-600 font-semibold text-indigo-600'
                    : 'text-gray-600'
                }`}
                onClick={() => setActiveTab('PDF')}
              >
                PDF
              </button>
              <button
                className={`pb-2 ${
                  activeTab === 'Textbook'
                    ? 'border-b-2 border-indigo-600 font-semibold text-indigo-600'
                    : 'text-gray-600'
                }`}
                onClick={() => setActiveTab('Textbook')}
              >
                Textbook
              </button>
            </div>

            {/* Tab Content */}
            <div className="bg-gray-200 h-[600px] flex items-center justify-center">
              {activeTab === 'PDF' ? (
                <iframe
                  src={pdfURL}
                  width="100%"
                  height="100%"
                  frameBorder="0"
                ></iframe>
              ) : (
                <iframe
                  src={textbookLink}
                  width="100%"
                  height="100%"
                  frameBorder="0"
                ></iframe>
              )}
            </div>
            <div className="mt-4 flex space-x-2">
              <a
                href={pdfURL}
                download
                className="bg-indigo-600 text-white px-4 py-2 rounded flex items-center hover:bg-indigo-700"
              >
                <Download className="mr-2 h-4 w-4" /> Download PDF
              </a>
              <button
                className="border border-gray-300 px-4 py-2 rounded hover:bg-gray-100"
                onClick={handleTakeQuiz}
              >
                Take Quiz
              </button>
            </div>
          </div>

          {/* Related Videos */}
          <div className="bg-white border rounded-lg p-4 shadow">
            <h2 className="text-xl font-semibold mb-4 text-indigo-700">
              Related Videos
            </h2>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              {videos && videos.length > 0 ? (
                videos.map((videoList, idx) =>
                  videoList.map((video, index) => (
                    <div
                      key={`${idx}-${index}`}
                      className="bg-gray-100 flex flex-col items-center justify-center p-2 rounded shadow"
                    >
                      <iframe
                        width="100%"
                        height="200"
                        src={`https://www.youtube.com/embed/${video.videoId}`}
                        frameBorder="0"
                        allowFullScreen
                      ></iframe>
                      <p className="text-center mt-2 text-gray-700">
                        {video.title}
                      </p>
                    </div>
                  ))
                )
              ) : (
                <p>No related videos found.</p>
              )}
            </div>
          </div>
        </div>

        {/* Sidebar */}
        <div className="space-y-6">
          {/* Summary */}
          <div className="bg-white border rounded-lg p-4 shadow">
            <h2 className="text-xl font-semibold mb-2 text-indigo-700">
              Summary
            </h2>
            <p className="text-gray-700">{summary}</p>
          </div>

          {/* Glossary */}
          <div className="bg-white border rounded-lg p-4 shadow">
            <h2 className="text-xl font-semibold mb-2 text-indigo-700">
              Glossary
            </h2>
            <div className="flex mb-2">
              <input
                type="text"
                placeholder="Search terms..."
                value={searchTerm}
                onChange={handleSearch}
                className="flex-grow border rounded-l px-3 py-2 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
              />
              <button className="bg-indigo-600 px-3 py-2 rounded-r text-white">
                <Search className="h-5 w-5" />
              </button>
            </div>
            <div className="h-40 overflow-y-auto">
              <ul className="space-y-2">
                {filteredGlossary.length > 0 ? (
                  filteredGlossary.map((item, idx) => (
                    <li key={idx}>
                      <span className="font-medium text-gray-800">
                        {item.term}:
                      </span>{' '}
                      <span className="text-gray-600">{item.definition}</span>
                    </li>
                  ))
                ) : (
                  <p>No terms found.</p>
                )}
              </ul>
            </div>
          </div>

          {/* Chat Interface */}
          <div className="bg-white border rounded-lg p-4 shadow">
            <h2 className="text-xl font-semibold mb-2 text-indigo-700">
              Ask a Question
            </h2>
            <div className="h-40 mb-2 overflow-y-auto border rounded p-2 bg-gray-50">
              {chatMessages.map((msg, index) => (
                <div
                  key={index}
                  className={`mb-2 ${
                    msg.sender === 'user' ? 'text-right' : 'text-left'
                  }`}
                >
                  <span
                    className={`inline-block p-2 rounded-lg ${
                      msg.sender === 'user'
                        ? 'bg-indigo-100 text-indigo-700'
                        : 'bg-gray-200 text-gray-700'
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
                className="flex-grow border rounded-l px-3 py-2 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
              />
              <button
                type="submit"
                className="bg-indigo-600 px-3 py-2 rounded-r text-white"
              >
                <MessageSquare className="h-5 w-5" />
              </button>
            </form>
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
      <div className="min-h-screen bg-gradient-to-br from-blue-100 to-indigo-100 flex flex-col items-center justify-center p-4">
        <div className="bg-white rounded-lg shadow-xl p-8 max-w-lg w-full text-center">
          <h1 className="text-2xl font-bold mb-4 text-indigo-700">
            Loading Quizzes...
          </h1>
          <div className="flex flex-col items-center space-y-4">
            <div className="animate-spin rounded-full h-16 w-16 border-t-4 border-b-4 border-indigo-600"></div>
            <span className="text-lg font-medium text-gray-700">
              Please wait a moment.
            </span>
          </div>
        </div>
      </div>
    );
  }

  // Display score after submission
  if (score !== null) {
    return (
      <div className="min-h-screen bg-gray-50 flex flex-col items-center justify-center p-4">
        <div className="bg-white rounded-lg shadow-xl p-8 max-w-md w-full text-center">
          <h1 className="text-2xl font-bold mb-4 text-indigo-700">
            Quiz Completed!
          </h1>
          <p className="text-lg text-gray-700 mb-6">
            Your Score: {score} / {Object.keys(quizzes).length}
          </p>
          <button
            onClick={() => navigate('/dashboard')}
            className="w-full bg-indigo-600 text-white px-4 py-2 rounded hover:bg-indigo-700"
          >
            Go Home
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50 p-4">
      <div className="max-w-3xl mx-auto bg-white p-6 rounded-lg shadow">
        <h1 className="text-3xl font-bold mb-6 text-indigo-700 text-center">
          Quiz
        </h1>
        <form onSubmit={handleSubmit} className="space-y-6">
          {/* Multiple Choice Questions */}
          <div>
            {Object.keys(quizzes).map((qKey, index) => {
              const questionData = quizzes[qKey];
              const question = questionData.question;
              const answers = [
                ...questionData.wrong_answers,
                questionData.correct_answer,
              ].sort();

              return (
                <div key={qKey} className="mb-6">
                  <p className="font-medium text-lg text-gray-800 mb-2">
                    {index + 1}. {question}
                  </p>
                  <div className="ml-4 space-y-2">
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
          <button
            type="submit"
            className="w-full bg-indigo-600 text-white px-4 py-2 rounded hover:bg-indigo-700"
          >
            Submit Quiz
          </button>
        </form>
      </div>
    </div>
  );
}