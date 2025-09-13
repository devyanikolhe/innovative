
        // Mobile menu toggle
        document.getElementById('mobile-toggle').addEventListener('click', function() {
            document.getElementById('nav-menu').classList.toggle('active');
        });
        
        // Close mobile menu when clicking on a link
        document.querySelectorAll('.nav-menu a').forEach(link => {
            link.addEventListener('click', function() {
                document.getElementById('nav-menu').classList.remove('active');
            });
        });
        
        // Smooth scrolling for anchor links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function(e) {
                e.preventDefault();
                
                const targetId = this.getAttribute('href');
                if (targetId === '#') return;
                
                const targetElement = document.querySelector(targetId);
                if (targetElement) {
                    window.scrollTo({
                        top: targetElement.offsetTop - 80,
                        behavior: 'smooth'
                    });
                }
            });
        });
        
        // Animation on scroll
        const fadeElements = document.querySelectorAll('.fade-in');
        
        const elementInView = (el, scrollOffset = 0) => {
            const elementTop = el.getBoundingClientRect().top;
            return (
                elementTop <= 
                (window.innerHeight || document.documentElement.clientHeight) - scrollOffset
            );
        };
        
        const displayScrollElement = (element) => {
            element.style.opacity = 1;
            element.style.transform = 'translateY(0)';
        };
        
        const hideScrollElement = (element) => {
            element.style.opacity = 0;
            element.style.transform = 'translateY(20px)';
        };
        
        const handleScrollAnimation = () => {
            fadeElements.forEach((el) => {
                if (elementInView(el, 100)) {
                    displayScrollElement(el);
                } else {
                    hideScrollElement(el);
                }
            });
        };
        
        window.addEventListener('scroll', () => {
            handleScrollAnimation();
        });
        
        // Initialize elements for animation
        window.addEventListener('load', function() {
            fadeElements.forEach(el => {
                el.style.opacity = 0;
                el.style.transform = 'translateY(20px)';
                el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            });
            
            handleScrollAnimation();
        });
    