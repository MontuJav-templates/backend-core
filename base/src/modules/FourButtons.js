import React, { useState } from 'react';
import Button from 'react-bootstrap/Button';

function FourButtons() {
    const [selectedFile, setSelectedFile] = useState(null);
  
    const handleFileSelect = (event) => {
      setSelectedFile(event.target.files[0]);
    };

    const processFile = async () => {
        if (!selectedFile) {
            console.log("No file selected");
            return
        }
        
        const fd = new FormData();
        fd.append('file', selectedFile);

        try {
            const response = await fetch('http://localhost:5000/process-las', {
                method: 'POST',
                body: fd,
            })

            const data = await response.json();

            console.log('Response:', data);

            if (data.status === 'success') {
                console.log('successful');
            } else {
                console.log('failed');
            }
        } catch (error) {
            console.log('ERROR:', error);
        }
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
