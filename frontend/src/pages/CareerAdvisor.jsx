import axios from "axios"
import {useState} from "react"

function CareerAdvisor(){

const [skills,setSkills] = useState("")
const [result,setResult] = useState("")

const getAdvice = async ()=>{

const res = await axios.post(
"http://localhost:8000/career-advice",
{skills:skills}
)

setResult(res.data.career_plan)

}

return(

<div>

<h2>Career Advisor</h2>

<input
placeholder="Enter your skills"
onChange={(e)=>setSkills(e.target.value)}
/>

<button onClick={getAdvice}>
Get Career Advice
</button>

<pre>{result}</pre>

</div>

)

}

export default CareerAdvisor