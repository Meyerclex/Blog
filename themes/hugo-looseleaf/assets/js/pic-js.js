document.addEventListener('DOMContentLoaded', () => {
    console.log('JavaScript loaded and DOMContentLoaded event fired.');

    const postContent = document.querySelector('#post-content');
    if (!postContent) {
        console.error('Error: #post-content not found!');
        return;
    }

    // 居中含图段落
    const paragraphs = postContent.querySelectorAll('p');
    paragraphs.forEach((paragraph) => {
        const img = paragraph.querySelector('img');
        if (img && img.id !== 'emoji') {
            paragraph.style.textAlign = 'center';
            paragraph.style.fontSize = '90%';
        }
    });

    // 处理不是 <p> 里的单张 img + 后文本
    const imgs = postContent.querySelectorAll('img');
    imgs.forEach((img) => {
        if (img.closest('p')) return; // 忽略被 <p> 包裹的图
        if (img.id === 'emoji') return;
        if (!img.alt) return;

        const next = img.nextSibling;
        if (next && next.nodeType === Node.TEXT_NODE && next.textContent.trim()) {
            const span = document.createElement('span');
            span.textContent = next.textContent.trim();
            span.style.display = 'block';
            span.style.textAlign = 'center';
            span.style.fontSize = '90%';
            img.parentNode.replaceChild(span, next);
        }
    });

    // 初始化图片点击放大功能的遮罩
    const overlay = document.createElement('div');
    overlay.className = 'image-overlay';
    document.body.appendChild(overlay);

    const overlayImage = document.createElement('img');
    overlay.appendChild(overlayImage);

    overlay.addEventListener('click', () => {
        overlay.classList.remove('active');
    });

    // 加载完成后给图片加 width/height，防止 Safari 排版乱
    function fixImageSize(img) {
        if (!img.hasAttribute('width')) {
            img.setAttribute('width', img.naturalWidth);
        }
        if (!img.hasAttribute('height')) {
            img.setAttribute('height', img.naturalHeight);
        }
    }

    // 点击图片放大
    const enableImageZoom = (img) => {
        if (!img.src.includes('/img/emoji/')) {
            img.style.cursor = 'zoom-in';
            img.addEventListener('click', () => {
                overlayImage.removeAttribute('src');
                overlayImage.removeAttribute('width');
                overlayImage.removeAttribute('height');

                overlayImage.src = img.src;
                overlayImage.setAttribute('width', img.width);
                overlayImage.setAttribute('height', img.height);

                overlayImage.style.width = 'auto';
                overlayImage.style.height = 'auto';

                overlay.classList.add('active');
            });
        }

        // 给图片加上 width/height
        if (img.complete) {
            fixImageSize(img);
        } else {
            img.addEventListener('load', () => fixImageSize(img));
        }
    };

    // 处理所有图片
    const images = Array.from(postContent.querySelectorAll('img'));
    if (images.length === 0) {
        console.log('No images found.');
        return;
    }
    console.log(`Found ${images.length} images.`);

    images.forEach(enableImageZoom);
});