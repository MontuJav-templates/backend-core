import React, { useState } from 'react';
import Button from 'react-bootstrap/Button';

function FourButtons() {
    const [selectedFile, setSelectedFile] = useState(null);
  
    const handleFileSelect = (event) => {
      setSelectedFile(event.target.files[0]);
    };

    const processFile = () => {
        console.log(selectedFile);
    }

    return (
        <div>
        <input type="file" onChange={handleFileSelect} />
        <br></br>
        <Button variant="secondary" onClick={processFile}>Process LAS file</Button>{' '}
        <Button variant="success">Plot crossplot</Button>{' '}
        <Button variant="danger">Cluster crossplot</Button>{' '}
        </div>
    );
}

export default FourButtons;
