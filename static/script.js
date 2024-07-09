document.getElementById('theme-toggle').addEventListener('change', function () {
    document.body.classList.toggle('dark-mode');
});

function previewImage() {
    const file = document.getElementById('image-upload').files[0];
    const reader = new FileReader();
    reader.onloadend = function () {
        const img = document.getElementById('image-preview');
        img.src = reader.result;
        img.style.display = 'block';
    }
    if (file) {
        reader.readAsDataURL(file);
    } else {
        const img = document.getElementById('image-preview');
        img.src = '';
        img.style.display = 'none';
    }
}

async function submitText() {
    const text = document.getElementById('text-input').value;
    const response = await fetch('/predict_text', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text })
    });
    const data = await response.json();
    document.getElementById('output').innerHTML = `<p>Sentiment: ${data.sentiment}</p><p>${data.motivation}</p>`;
}

async function submitImage() {
    const file = document.getElementById('image-upload').files[0];
    const formData = new FormData();
    formData.append('file', file);

    const response = await fetch('/predict_image', {
        method: 'POST',
        body: formData
    });

    const data = await response.json();
    document.getElementById('output').innerHTML = `<p>Sentiment: ${data.sentiment}</p><p>${data.motivation}</p>`;
}
