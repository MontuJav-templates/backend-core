import React from 'react';
import Button from 'react-bootstrap/Button';

function FourButtons() {
  return (
    <div>
      <Button variant="primary">Upload LAS file</Button>{' '}
      <Button variant="secondary">Process LAS file</Button>{' '}
      <Button variant="success">Plot crossplot</Button>{' '}
      <Button variant="danger">Cluster crossplot</Button>{' '}
    </div>
  );
}

export default FourButtons;
