document.addEventListener("DOMContentLoaded", () => {
    const body = document.body;
    const themeToggleButton = document.querySelector('.theme-toggle-button');
    const languageButtons = document.querySelectorAll('.language-button');

    // Butonların seçilip seçilmediğini kontrol et
    if (!themeToggleButton) {
        console.error('Tema butonu bulunamadı.');
        return;
    }

    if (languageButtons.length === 0) {
        console.error('Dil değiştirme butonları bulunamadı.');
        return;
    }

    // LocalStorage'dan kaydedilen temayı al ve uygula
    const savedTheme = localStorage.getItem('theme') || 'body-dark-tema';
    body.classList.add(savedTheme);

    // Temayı günceller ve buton yazısını değiştiren fonksiyon
    const updateThemeText = () => {
        const currentLang = new URL(window.location.href).searchParams.get('lang');
        
        if (currentLang === 'en') {
            themeToggleButton.textContent = body.classList.contains('body-dark-tema') 
                ? 'Switch to Light Mode' 
                : 'Switch to Dark Mode';
        } else if (currentLang === 'tr') {
            themeToggleButton.textContent = body.classList.contains('body-dark-tema') 
                ? 'Aydınlık Moda Geç' 
                : 'Karanlık Moda Geç';
        } else if (currentLang === 'ru') {
            themeToggleButton.textContent = body.classList.contains('body-dark-tema') 
                ? 'Переключиться на светлый режим' 
                : 'Переключиться на темный режим';
        } else if (currentLang === 'de') {
            themeToggleButton.textContent = body.classList.contains('body-dark-tema') 
                ? 'Wechseln Sie zum hellen Modus' 
                : 'Wechseln Sie zum dunklen Modus';
        }
    };

    // Sayfa yüklenirken temayı güncelle
    updateThemeText();

    // Tema değiştirme fonksiyonu
    const toggleTheme = () => {
        const isLightTheme = body.classList.contains('body-light-tema');
        body.classList.toggle('body-light-tema', !isLightTheme);
        body.classList.toggle('body-dark-tema', isLightTheme);

        // Yeni temayı LocalStorage'a kaydet
        localStorage.setItem('theme', isLightTheme ? 'body-dark-tema' : 'body-light-tema');
        
        // Temayı güncelle
        updateThemeText();
    };

    // Tema butonuna tıklama olayını dinle
    themeToggleButton.addEventListener('click', toggleTheme);

    // Dil değiştirme butonlarının işlevselliği
    const changeLanguage = (lang) => {
        const currentUrl = new URL(window.location.href);
        currentUrl.searchParams.set('lang', lang);
        window.location.href = currentUrl.toString();
    };

    languageButtons.forEach(button => {
        button.addEventListener('click', () => {
            const selectedLang = button.getAttribute('data-lang');
            if (selectedLang) {
                changeLanguage(selectedLang);
            } else {
                console.error('Dil bilgisi butonda tanımlı değil.');
            }
        });
    });

    // Yüklenme sırasında tarayıcı konsolunda temanın doğru yüklendiğini göster
    console.log(`Yüklenen tema: ${savedTheme}`);
});
