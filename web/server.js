"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const bun_1 = require("bun");
(0, bun_1.serve)({
    port: 3000,
    fetch(req) {
        const url = new URL(req.url);
        if (url.pathname === "/") {
            return new Response(Bun.file("./index.html"), {
                headers: { "Content-Type": "text/html" },
            });
        }
        return new Response("Not Found", { status: 404 });
    },
});
//# sourceMappingURL=server.js.map