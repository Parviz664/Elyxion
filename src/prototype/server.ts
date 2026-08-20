import { readFile } from "node:fs/promises";
import { createServer } from "node:http";
import { resolve } from "node:path";

interface PrototypeRoute {
  readonly file: string;
  readonly contentType: string;
}

// Fixed routes keep this prototype server small and avoid exposing other files.
const ROUTES: Readonly<Record<string, PrototypeRoute>> = Object.freeze({
  "/": {
    file: "prototype/index.html",
    contentType: "text/html; charset=utf-8",
  },
  "/prototype.css": {
    file: "prototype/prototype.css",
    contentType: "text/css; charset=utf-8",
  },
  "/app.js": {
    file: "dist/src/prototype/browser.js",
    contentType: "text/javascript; charset=utf-8",
  },
  "/friendly-point-evolution.js": {
    file: "dist/src/prototype/friendly-point-evolution.js",
    contentType: "text/javascript; charset=utf-8",
  },
  "/rhythm": {
    file: "prototype/rhythm.html",
    contentType: "text/html; charset=utf-8",
  },
  "/rhythm/": {
    file: "prototype/rhythm.html",
    contentType: "text/html; charset=utf-8",
  },
  "/rhythm.css": {
    file: "prototype/rhythm.css",
    contentType: "text/css; charset=utf-8",
  },
  "/rhythm.js": {
    file: "dist/src/prototype/rhythm-browser.js",
    contentType: "text/javascript; charset=utf-8",
  },
  "/manual-rhythm-cycle.js": {
    file: "dist/src/prototype/manual-rhythm-cycle.js",
    contentType: "text/javascript; charset=utf-8",
  },
});

const port = Number(process.env.PORT ?? 4173);

if (!Number.isInteger(port) || port <= 0 || port > 65_535) {
  throw new RangeError("PORT must be an integer from 1 to 65535.");
}

const server = createServer(async (request, response) => {
  const pathname = new URL(request.url ?? "/", "http://localhost").pathname;
  const route = ROUTES[pathname];

  if (route === undefined) {
    response.writeHead(404, { "content-type": "text/plain; charset=utf-8" });
    response.end("Not found");
    return;
  }

  try {
    const body = await readFile(resolve(process.cwd(), route.file));
    response.writeHead(200, { "content-type": route.contentType });
    response.end(body);
  } catch (error: unknown) {
    console.error("Failed to serve an Elyxion prototype resource.", error);
    response.writeHead(500, { "content-type": "text/plain; charset=utf-8" });
    response.end("Prototype file unavailable");
  }
});

server.listen(port, "127.0.0.1", () => {
  console.log(`Elyxion prototypes: http://localhost:${port}`);
  console.log(`Manual Rhythm TASK 002: http://localhost:${port}/rhythm`);
});
