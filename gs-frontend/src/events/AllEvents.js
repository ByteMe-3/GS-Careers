import * as React from 'react';
import Link from '@mui/material/Link';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Title from '../components/Title';

// Generate Order Data
function createData(id, event, category, division,date, location) {
  return { id, event, category, division,date, location };
}

const rows = [
  createData(
    0,
    'RTC Exploratory Programs',
    'Divisional',
    'Engineering',
    '28-Jul-2022',
    'Virtual',
  ),
  createData(
    1,
    '2023 MBA Fellowship',
    'Diversity',
    'Consumer and Wealth Management, Investment Banking Division',
    '22-Aug-2022',
    'All Americas Offices',
  ),
  createData(
    2,
    'RTC Exploratory Programs',
    'Divisional',
    'Engineering',
    '28-Jul-2022',
    'Virtual',
  ),
  createData(
    3,
    '2023 MBA Fellowship',
    'Diversity',
    'Consumer and Wealth Management, Investment Banking Division',
    '22-Aug-2022',
    'All Americas Offices',
  ),
  createData(
    4,
    'RTC Exploratory Programs',
    'Divisional',
    'Engineering',
    '28-Jul-2022',
    'Virtual',
  ),
  createData(
    5,
    '2023 MBA Fellowship',
    'Diversity',
    'Consumer and Wealth Management, Investment Banking Division',
    '22-Aug-2022',
    'All Americas Offices',
  ),
  createData(
    6,
    'RTC Exploratory Programs',
    'Divisional',
    'Engineering',
    '28-Jul-2022',
    'Virtual',
  ),
  createData(
    7,
    '2023 MBA Fellowship',
    'Diversity',
    'Consumer and Wealth Management, Investment Banking Division',
    '22-Aug-2022',
    'All Americas Offices',
  )
];

function preventDefault(event) {
  event.preventDefault();
}

export default function AllEvents() {
  return (
    <React.Fragment>
      <Title>Upcoming events</Title>
      <Table size="small">
        <TableHead>
          <TableRow>
            <TableCell>Event</TableCell>
            <TableCell>Category</TableCell>
            <TableCell>Division</TableCell>
            <TableCell>Date</TableCell>
            <TableCell align="right">Location</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow key={row.id}>
              <TableCell>{row.event}</TableCell>
              <TableCell>{row.category}</TableCell>
              <TableCell>{row.division}</TableCell>
              <TableCell>{row.date}</TableCell>
              <TableCell align="right">{row.location}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </React.Fragment>
  );
}
