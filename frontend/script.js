async function uploadAndPredict() {
  const fileInput = document.getElementById('fileInput');
  const formData = new FormData();
  
  if (!fileInput.files.length) {
    alert("Please select a file first.");
    return;
  }

  formData.append("file", fileInput.files[0]);

  try {
    const response = await fetch("/predict", {
      method: "POST",
      body: formData
    });

    if (!response.ok) {
      throw new Error(`Server responded with ${response.status}`);
    }

    const result = await response.json();
    console.log("Prediction result:", result);

    document.getElementById("predictionResult").innerHTML = `
      <h4>Prediction: ${result.label}</h4>
      <p>Confidence: ${result.confidence.toFixed(2)}</p>
    `;
  } catch (error) {
    console.error("Prediction error:", error);
    document.getElementById("predictionResult").innerHTML = `
      <div class="alert alert-danger">Error occurred: ${error.message}</div>
    `;
  }
}
