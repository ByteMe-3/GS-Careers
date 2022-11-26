import './App.css';
import Dashboard from './dashboard/Dashboard';
import EarnPoints from './earnpoints/EarnPoints';
import { HashRouter, Route, Routes } from 'react-router-dom';
import Events from './events/Events';
import Profile from './components/profile';
import Quiz from './components/quiz';

function App() {
  return (
    <HashRouter>
      <Routes>
          <Route path='/' element={<Dashboard />}></Route>
          <Route path='/earnpoints' element={<EarnPoints/>}></Route>
          <Route path='/events' element={<Events/>}></Route>
          <Route path='/quiz' element={<Quiz/>}></Route>
          <Route path='/profile' element={<Profile/>}></Route>
      </Routes>
    </HashRouter>
  );
}

export default App;
