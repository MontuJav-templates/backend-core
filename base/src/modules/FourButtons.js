import React from 'react';
import Button from 'react-bootstrap/Button';

function FourButtons() {
    const handleClick = () => {
        console.log('Hello, world!');
    };

    return (
        <div>
        <Button variant="primary" onClick={handleClick}>Upload LAS file</Button>{' '}
        <Button variant="secondary">Process LAS file</Button>{' '}
        <Button variant="success">Plot crossplot</Button>{' '}
        <Button variant="danger">Cluster crossplot</Button>{' '}
        </div>
    );
}

export default FourButtons;
