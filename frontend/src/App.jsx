import "./App.css";

import Dashboard from "./pages/Dashboard";
import ResumeAnalyzer from "./pages/ResumeAnalyzer";
import CareerAdvisor from "./pages/CareerAdvisor";

function App() {

  return (
    <div className="app">

      <div className="header">
        <h1>VidyaMitra AI Career Assistant</h1>
        <p>AI-powered resume analysis and career guidance</p>
      </div>

      <div className="grid">

        <div className="card">
          <Dashboard />
        </div>

        <div className="card">
          <ResumeAnalyzer />
        </div>

        <div className="card">
          <CareerAdvisor />
        </div>

      </div>

    </div>
  );
}

export default App;