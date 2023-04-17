import React from 'react';

function UploadButton(props) {
  const fileInputRef = React.createRef();

  const handleButtonClick = () => {
    fileInputRef.current.click();
  };

  const handleFileInputChange = (event) => {
    const selectedFile = event.target.files[0];
    props.onFileSelect(selectedFile);
    console.log(selectedFile);
  };

  return (
    <div>
      <button onClick={handleButtonClick}>Select File</button>
      <input type="file" onChange={handleFileInputChange} ref={fileInputRef} style={{ display: 'none' }} />
    </div>
  );
}

export default UploadButton;
