import logo from './logo.svg';
import './App.css';
import Dashboard from './dashboard/Dashboard';
import EarnPoints from './earnpoints/EarnPoints';
import { HashRouter, Route, Routes } from 'react-router-dom';
import Events from './events/Events';
import Profile from './components/profile';

function App() {
  return (
    <HashRouter>
      <Routes>
          <Route path='/' element={<Dashboard />}></Route>
          <Route path='/earnpoints' element={<EarnPoints/>}></Route>
          <Route path='/events' element={<Events/>}></Route>
          <Route path='/profile' element={<Profile/>}></Route>
          {/* <Route path='/task/:id' element={<div><HomePage/></div>}></Route> */}
          {/*
          
          <Route path='/profile' element={<div><LoginPage/></div>}></Route>
          <Route path='/backlog' element={<div><LoginPage/></div>}></Route>
          <Route path='/profile/:id' element={<div><ProfilePage/></div>}></Route> */}
      </Routes>
    </HashRouter>
  );
}

export default App;
