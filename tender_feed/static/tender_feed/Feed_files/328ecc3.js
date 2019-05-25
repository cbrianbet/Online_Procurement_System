(function(window) {
    var previousHandler = window.onerror;
    var errorCache = [];
    var errorKey;
    var jsLogPath = Applet.getBasePath() + '/public/api/v2/aux/log-js';

    window.onerror = function(message, source, line, col, error) {
        errorKey = message + source + line + col;
        if ((errorCache.indexOf(errorKey) === -1) && (errorCache.length < 100)) {
            errorCache.push(errorKey);

            var stack = [];
            if (typeof error === 'string') {
                // Component library's own exception handler passes stack
                // stringinstead of error object
                stack = error.split('\n').map(function(line) {
                    return line.trim();
                });
            } else if (error && error.stack) {
                stack = error.stack.split('\n').map(function(line) {
                    return line.trim();
                });
            }

            try {
                var params = {
                    message: message,
                    source:  source,
                    line:    line,
                    col:     col,
                    stack:   stack,
                    cookieLength: document.cookie.length,
                    userUid: (window.Applet && window.Applet.getUser()) ? window.Applet.getUser().getUid() : null,
                    page_runtime_id: window.Applet ? window.Applet.getVar('runtime_id') : null
                };

                var xmlhttp = new XMLHttpRequest();
                xmlhttp.open('POST', jsLogPath, true);
                xmlhttp.setRequestHeader('Content-type', 'application/json;charset=UTF-8');
                xmlhttp.send(JSON.stringify(params));
            } catch (e) {
                if (window.console && typeof window.console.error === 'function') {
                    window.console.error(e);
                }
            }
        }
        if (previousHandler) {
            previousHandler.apply(this, arguments);
        }
    };
})(window);