document.addEventListener('DOMContentLoaded', function() {
    const toggleButton = document.getElementById('theme-toggle');
    const currentTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', currentTheme);

    if (currentTheme === 'dark') {
        document.getElementById('theme-toggle').innerText = 'Switch to Light Mode';
    } else {
        document.getElementById('theme-toggle').innerText = 'Switch to Dark Mode';
    }

    toggleButton.addEventListener('click', function() {
        let theme = document.documentElement.getAttribute('data-theme');
        if (theme === 'light') {
            theme = 'dark';
            document.getElementById('theme-toggle').innerText = 'Switch to Light Mode';
        } else {
            theme = 'light';
            document.getElementById('theme-toggle').innerText = 'Switch to Dark Mode';
        }
        document.documentElement.setAttribute('data-theme', theme);
        localStorage.setItem('theme', theme);
    });
});
