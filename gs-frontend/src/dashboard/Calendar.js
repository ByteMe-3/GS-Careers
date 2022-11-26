import * as React from 'react';
import { useTheme } from '@mui/material/styles';
import Calendar from 'react-calendar';
import Title from '../components/Title';
import 'react-calendar/dist/Calendar.css';

export default function CalendarGS() {
    return (
      <React.Fragment>
        <Title>Events summary</Title>
        <Calendar 
            locale="EN-US"/>
      </React.Fragment>
    );
  }