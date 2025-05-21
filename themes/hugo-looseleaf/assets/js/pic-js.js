document.addEventListener('DOMContentLoaded', () => {
    console.log('JavaScript loaded and DOMContentLoaded event fired.');

    const postContent = document.querySelector('#post-content');
    if (!postContent) {
        console.error('Error: #post-content not found!');
        // 如果这里打印了错误，说明您的文章内容区域ID不是 #post-content
        // 您需要检查您的主题布局文件，确认文章内容区域的正确ID，并修改此处
        return;
    }

    // --- 辅助函数：加载完成后给图片加 width/height，防止 Safari 排版乱 ---
    // 这个函数现在只会处理非 emoji 的图片
    function fixImageSize(img) {
        // 如果是 Twemoji 生成的 emoji，则跳过尺寸修正
        if (img.classList.contains('emoji')) {
            return;
        }
        if (!img.hasAttribute('width')) {
            img.setAttribute('width', img.naturalWidth);
        }
        if (!img.hasAttribute('height')) {
            img.setAttribute('height', img.naturalHeight);
        }
    }

    // --- 辅助函数：点击图片放大功能 ---
    // 这个函数现在只会处理非 emoji 的图片，并根据 src 路径判断是否放大
    const enableImageZoom = (img) => {
        // 如果是 Twemoji 生成的 emoji，则跳过所有放大相关的处理
        if (img.classList.contains('emoji')) {
            return;
        }

        // 仅当图片 src 不包含 '/img/emoji/' 时，才添加点击放大功能和光标样式
        // 这保留了您原始脚本对特定图片路径的排除逻辑
        if (!img.src.includes('/img/emoji/')) {
            img.style.cursor = 'zoom-in';
            img.addEventListener('click', () => {
                overlayImage.removeAttribute('src');
                overlayImage.removeAttribute('width');
                overlayImage.removeAttribute('height');

                overlayImage.src = img.src;
                overlayImage.setAttribute('width', img.width);
                overlayImage.setAttribute('height', img.height);

                overlayImage.style.width = 'auto'; // 确保弹出的图片尺寸自适应
                overlayImage.style.height = 'auto';

                overlay.classList.add('active');
            });
        }

        // 加载完成后给所有非 emoji 图片加上 width/height，无论它们是否可以放大
        // fixImageSize 函数内部已包含对 emoji 的排除
        if (img.complete) {
            fixImageSize(img);
        } else {
            img.addEventListener('load', () => fixImageSize(img));
        }
    };

    // --- 初始化图片点击放大功能的遮罩 ---
    const overlay = document.createElement('div');
    overlay.className = 'image-overlay';
    document.body.appendChild(overlay);

    const overlayImage = document.createElement('img');
    overlay.appendChild(overlayImage);

    overlay.addEventListener('click', () => {
        overlay.classList.remove('active');
    });


    // --- 主要逻辑：处理文章内容中的所有图片 ---
    const images = Array.from(postContent.querySelectorAll('img'));
    if (images.length === 0) {
        console.log('No images found.');
        return;
    }
    console.log(`Found ${images.length} images.`);

    // 遍历所有图片，并应用 enableImageZoom 逻辑
    images.forEach(enableImageZoom);


    // --- 额外：处理段落和非 <p> 内图片（这些逻辑与 emoji 无关，保持原样） ---
    // 居中含图段落
    const paragraphs = postContent.querySelectorAll('p');
    paragraphs.forEach((paragraph) => {
        const img = paragraph.querySelector('img');
        // 确保这里也排除 class="emoji" 的图片，以免影响 emoji 所在段落
        if (img && img.id !== 'emoji' && !img.classList.contains('emoji')) {
            paragraph.style.textAlign = 'center';
            paragraph.style.fontSize = '90%';
        }
    });

    // 处理不是 <p> 里的单张 img + 后文本
    const imgsInContent = postContent.querySelectorAll('img'); // 重新获取一次，确保是当前状态的 img
    imgsInContent.forEach((img) => {
        // 排除 class="emoji" 的图片
        if (img.classList.contains('emoji')) return;
        if (img.closest('p')) return; // 忽略被 <p> 包裹的图
        if (img.id === 'emoji') return; // 这个条件可能可以被 img.classList.contains('emoji') 替代
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
});