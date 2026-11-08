import React from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import { ThemeProvider } from "./context/ThemeContext";
import { InterviewProvider, useInterviewContext } from "./context/InterviewContext";
import Navbar from "./components/Navbar";
import Notification from "./components/Notification";

import LandingPage from "./pages/LandingPage";
import DashboardPage from "./pages/DashboardPage";
import InterviewSetupPage from "./pages/InterviewSetupPage";
import LiveInterviewPage from "./pages/LiveInterviewPage";
import EvaluationPage from "./pages/EvaluationPage";
import HistoryPage from "./pages/HistoryPage";
import RoadmapPage from "./pages/RoadmapPage";
import ProfilePage from "./pages/ProfilePage";

function AppContent() {
  const { error, clearError } = useInterviewContext();

  return (
    <div className="min-h-screen flex flex-col bg-[#F9F8FD] dark:bg-navy-950 text-slate-800 dark:text-slate-100 transition-colors duration-200">
      <Navbar />

      <main className="flex-1 overflow-y-auto">
        <Routes>
          <Route path="/" element={<LandingPage />} />
          <Route path="/dashboard" element={<DashboardPage />} />
          <Route path="/setup" element={<InterviewSetupPage />} />
          <Route path="/interview" element={<LiveInterviewPage />} />
          <Route path="/evaluation" element={<EvaluationPage />} />
          <Route path="/history" element={<HistoryPage />} />
          <Route path="/roadmap" element={<RoadmapPage />} />
          <Route path="/profile" element={<ProfilePage />} />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </main>

      {error && <Notification type="error" message={error} onClose={clearError} />}
    </div>
  );
}

export function App() {
  return (
    <ThemeProvider>
      <InterviewProvider>
        <Router>
          <AppContent />
        </Router>
      </InterviewProvider>
    </ThemeProvider>
  );
}

export default App;
