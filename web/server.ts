import { serve } from "bun";

serve({
  port: 8022,
  fetch(req) {
    const url = new URL(req.url);
    if (url.pathname === "/") {
      return new Response(Bun.file("./index.html"), {
        headers: { "Content-Type": "text/html" },
      });
    } else if (url.pathname === "/src/style.css") {
      return new Response(Bun.file("./src/style.css"), {
        headers: { "Content-Type": "text/css" },
      });
    } else if (url.pathname === "/src/main.js") {
      return new Response(Bun.file("./src/main.js"), {
        headers: { "Content-Type": "text/javascript" },
      });
    }
    return new Response("Not Found", { status: 404 });
  },
});
