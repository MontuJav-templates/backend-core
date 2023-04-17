import React, { useState } from 'react';
import Button from 'react-bootstrap/Button';
import UploadButton from './buttons/UploadButton';

function FourButtons() {
    const [selectedFile, setSelectedFile] = useState(null);
  
    const handleFileSelect = (file) => {
      setSelectedFile(file);
      console.log(selectedFile);
      // TODO: Upload file
    };

    return (
        <div>
        <UploadButton onFileSelect={handleFileSelect} />
        <Button variant="secondary">Process LAS file</Button>{' '}
        <Button variant="success">Plot crossplot</Button>{' '}
        <Button variant="danger">Cluster crossplot</Button>{' '}
        </div>
    );
}

export default FourButtons;
