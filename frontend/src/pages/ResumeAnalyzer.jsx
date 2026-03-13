import { useState } from "react";
import axios from "axios";

function ResumeAnalyzer(){

  const [file, setFile] = useState(null);
  const [result, setResult] = useState("");

  const analyze = async () => {

    if(!file){
      alert("Please upload a PDF first");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {

      console.log("Sending file to backend...");

      const res = await axios.post(
        "http://localhost:8000/resume-analysis",
        formData,
        {
          headers:{
            "Content-Type":"multipart/form-data"
          }
        }
      );

      console.log("Response:", res.data);

      setResult(res.data.analysis);

    } catch (error) {

      console.error("Error:", error);

      alert("Resume analysis failed. Check backend.");

    }

  };

  return(

    <div>

      <h2>Resume Analyzer</h2>

      <input
        type="file"
        accept=".pdf"
        onChange={(e)=>setFile(e.target.files[0])}
      />

      <br/><br/>

      <button onClick={analyze}>
        Analyze Resume
      </button>

      <pre>{result}</pre>

    </div>

  );

}

export default ResumeAnalyzer;