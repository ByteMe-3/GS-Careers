import * as React from 'react';
import Link from '@mui/material/Link';
import Typography from '@mui/material/Typography';
import Title from '../components/Title';

function preventDefault(event) {
  event.preventDefault();
}

export default function Deposits() {
  return (
    <React.Fragment>
      <Title>My points</Title>
      <Typography component="p" variant="h4">
        130
      </Typography>
      <div>
        <Link color="primary" href="#" onClick={preventDefault}>
          View points history
        </Link>
      </div>
    </React.Fragment>
  );
}
