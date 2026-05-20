import os

css_path = "c:\\My Web Sites\\ajnets\\style.css"
css_content = """

/* Modal Styling */
.modal-overlay {
    display: none;
    position: fixed;
    z-index: 1050;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0,0,0,0.6);
}

.modal-content {
    background-color: #fff;
    margin: 15% auto;
    padding: 40px 20px;
    border: 0;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    width: 90%;
    max-width: 500px;
    text-align: center;
    border-radius: 12px;
    position: relative;
}

.close-modal {
    color: #888;
    position: absolute;
    right: 20px;
    top: 15px;
    font-size: 28px;
    font-weight: bold;
    cursor: pointer;
}

.modal-success-icon {
    font-size: 50px;
    color: #2ecc71;
    margin-bottom: 20px;
}

.modal-content h2 {
    margin-bottom: 15px;
    font-size: 28px;
    color: #333;
}

.modal-content p {
    color: #666;
    font-size: 16px;
}
"""

with open(css_path, 'a', encoding='utf-8') as f:
    f.write(css_content)

print("Appended modal CSS to style.css")
