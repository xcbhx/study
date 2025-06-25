function handleEmail(event) {
    event.preventDefault();

    const subject = encodeURIComponent(document.getElementById('subject').value);
    const body = encodeURIComponent(document.getElementById('body').value);
    const mailtoLink = `mailto:lucila.hernandezdelcarmen@students.dominican.edu?subject=${subject}&body=${body}`;

    window.location.href = mailtoLink;
}
