import React, { useEffect, useState } from 'react';
import './quiz.css'
import axios from 'axios';

export default function Quiz() {
	axios.defaults.xsrfCookieName = 'csrftoken'
	axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
import { Button } from '@mui/material';

export default function Quiz() {
	const [currentQuestion, setCurrentQuestion] = useState(0);
	const [showScore, setShowScore] = useState(false);
	const [score, setScore] = useState(0);
	const [questions, setQuestions] = useState();
	const [chosenAnswers, ChosenAnswers] = useState([]);
	const [showMessage, setMessage] = useState();
	const handleAnswerOptionClick = (param, que) => {
		ChosenAnswers((prevArray) => [...prevArray, {'answer': param, 'id': que}])
		const nextQuestion = currentQuestion + 1;
		if (nextQuestion < questions.length) {
			setCurrentQuestion(nextQuestion);
		} else {
			setShowScore(true);
		}
	};

	const fetchQuizData = () => {
		axios.get('api/quiz/').then(res => setQuestions(res.data));
	  }

	  useEffect(() => {
		fetchQuizData()
	  }, []);
	
	  useEffect(() => {
		if(showScore)
		{
			axios.post('api/quiz/', chosenAnswers).then(res => setMessage(res.data))
		}
	  }, [chosenAnswers, showScore]);

	  if(questions !== undefined)
	  {
		console.log(questions[0].answers)
		return (
			<div className='app'>
				{showScore ? (
					<div className='score-section'>
						{showMessage}
					</div>
				) : (
					<>
						<div className='question-section'>
							<div className='question-count'>
								<span>Question {currentQuestion + 1}</span>/{questions.length}
							</div>
							<div className='question-text'>{questions[currentQuestion].question}</div>
						</div>
						<div className='answer-section'>
							{questions[currentQuestion].answers.map((answerOption) => (
								<Button sx={{elevation : 20}} className='button-answer' variant="contained" onClick={() => handleAnswerOptionClick(answerOption, questions[currentQuestion].id)}>{answerOption}</Button>
							))}
						</div>
					</>
				)}
			</div>
		);
	}
}