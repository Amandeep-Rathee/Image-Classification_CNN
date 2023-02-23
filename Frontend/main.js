const imageInput = document.getElementById('image-input');
const predictButton = document.getElementById('predict-button');
const resultElement = document.getElementById('result');

// Event listener for the "Predict" button
predictButton.addEventListener('click', () => {
  const imageFile = imageInput.files[0];
  if (imageFile) {
    // Create a FormData object to send the file to the API
    const formData = new FormData();
    formData.append('image', imageFile);

    // Send a POST request to the API endpoint
    fetch('http://127.0.0.1:5000/predict', {
      method: 'POST',
      body: formData
    })
    .then(response => response.json())
    .then(data => {
      // Update the UI with the prediction result
      resultElement.textContent = `Prediction: ${data.prediction}`;
    })
    .catch(error => {
      console.error(error);
      alert('An error occurred while making the prediction.');
    });
  } else {
    alert('Please select an image file.');
  }
});
