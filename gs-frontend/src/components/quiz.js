import React, { useEffect, useState } from 'react';
import './quiz.css'
import axios from 'axios';
export default function Quiz() {

	const [currentQuestion, setCurrentQuestion] = useState(0);
	const [showScore, setShowScore] = useState(false);
	const [score, setScore] = useState(0);
	const [questions, setQuestions] = useState();
	const [chosenAnswers, ChosenAnswers] = useState([]);
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
			axios.post('api/quiz/', chosenAnswers).then(res => console.log(res))
		}
	  }, [chosenAnswers, showScore]);

	  if(questions !== undefined)
	  {
		console.log(questions[0].answers)
		return (
			<div className='app'>
				{showScore ? (
					<div className='score-section'>
						You scored {score} out of {questions.length}
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
								<button className='button-answer' onClick={() => handleAnswerOptionClick(answerOption, questions[currentQuestion].id)}>{answerOption}</button>
							))}
						</div>
					</>
				)}
			</div>
		);
	}
}