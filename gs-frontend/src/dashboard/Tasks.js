import React, { useEffect, useState } from 'react';
import Link from '@mui/material/Link';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Title from '../components/Title';
import axios from 'axios';
// Generate Order Data
function createData(id, date, name, amount) {
  return { id, date, name, amount };
}

const rows = [
  createData(
    0,
    '16 Mar, 2019',
    'LinkedIn Share',
    20,
  ),
  createData(
    1,
    '16 Mar, 2019',
    'Event registration',
    50,
  ),
  createData(
    3,
    '16 Mar, 2019',
    'Withdrawn tshirt',
    -100,
  ),
  createData(
    1,
    '16 Mar, 2019',
    'Event registration',
    50,
  ),
  createData(
    3,
    '16 Mar, 2019',
    'Withdrawn tshirt',
    -100,
  ),
  createData(
    1,
    '16 Mar, 2019',
    'Event registration',
    50,
  ),
];

function preventDefault(event) {
  event.preventDefault();
}

export default function RecentTasks() {

  const [tasks, setTasks] = useState([])

  const fetchData = () => {
    axios.get('api/task/list/').then(res => setTasks(res.data));
  }

  useEffect(() => {
    fetchData()
  }, []);

  return (
    <React.Fragment>
      <Title>Recent operations</Title>
      <Table size="small">
        <TableHead>
          <TableRow>
            <TableCell>Date</TableCell>
            <TableCell>Operation</TableCell>
            <TableCell align="right">Sale Amount</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {tasks !== undefined && tasks.map((row) => (
            <TableRow key={row.id}>
              <TableCell>{row.date}</TableCell>
              <TableCell>{row.name}</TableCell>
              <TableCell align="right">{`${row.amount} points`}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
      <Link color="primary" href="/#/backlog" sx={{ mt: 3 }}>
        See more operations
      </Link>
    </React.Fragment>
  );
}
