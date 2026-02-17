# RPC failure "Network connection lost" with cloudflare python worker

## Running worker1
```
$ cd w1/
$ npx wrangler dev
npm warn Unknown user config "always-auth". This will stop working in the next major version of npm.

 ⛅️ wrangler 4.64.0
───────────────────
╭──────────────────────────────────────────────────────────────────────╮
│  [b] open a browser [d] open devtools [c] clear console [x] to exit  │
╰──────────────────────────────────────────────────────────────────────╯
⎔ Starting local server...
[wrangler:info] Ready on http://localhost:8788
```

## Running worker2
```
$ cd w2/
$ npx wrangler dev
npm warn Unknown user config "always-auth". This will stop working in the next major version of npm.

 ⛅️ wrangler 4.64.0
───────────────────
Your Worker has access to the following bindings:
Binding               Resource      Mode
env.W1 (worker1)      Worker        local [connected]


Service bindings, Durable Object bindings, and Tail consumers connect to other Wrangler or Vite dev processes running locally, with their connection status indicated by [connected] or [not connected]. For more details, refer to https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/#local-development

╭──────────────────────────────────────────────────────────────────────╮
│  [b] open a browser [d] open devtools [c] clear console [x] to exit  │
╰──────────────────────────────────────────────────────────────────────╯
⎔ Starting local server...
⎔ Connection status updated
Your Worker has access to the following bindings:
Binding               Resource      Mode
env.W1 (worker1)      Worker        local [connected]

[wrangler:info] Ready on http://localhost:8789
```

## After visiting w2 at `http://localhost:8789` we get the following error
```
[mf:error] Error: read ECONNRESET
    at TCP.onStreamRead (node:internal/stream_base_commons:216:20)
✘ [ERROR] Uncaught PythonError: Traceback (most recent call last):

    File "introspection.py", line 88, in wrapper_func
      return python_to_rpc(await result)
                           ^^^^^^^^^^^^
    File "/session/metadata/entry.py", line 5, in fetch
      res = await self.env.W1.add(1, 2)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "/lib/python3.13/site-packages/workers/_workers.py", line 1030, in wrapper
      return python_from_rpc(await result)
                             ^^^^^^^^^^^^
  pyodide.ffi.JsException: Error: Network connection lost.
   Error
      at new_error (pyodide-internal:generated/emscriptenSetup:19907:14)
      at [object Object]
      at [object Object]
      at [object Object]
      at [object Object]
      at [object Object]
      at [object Object]
      at [object Object]
      at [object Object]
      at [object Object]
      at [object Object]
      at [object Object]
      at [object Object]
      at [object Object]
      at [object Object]
      at [object Object]
      at wrapper (pyodide-internal:generated/emscriptenSetup:24630:28)
      at promisingApply2 (pyodide-internal:generated/emscriptenSetup:24615:16)
      at callPyObjectKwargsPromising (pyodide-internal:generated/emscriptenSetup:22418:60)
      at Module.callPyObjectMaybePromising (pyodide-internal:generated/emscriptenSetup:22441:47)
      at wrapper (pyodide-internal:generated/emscriptenSetup:20785:29)
      at e.port1.onmessage (pyodide-internal:generated/emscriptenSetup:24117:75)


✘ [ERROR] Uncaught Error: Traceback (most recent call last):

    File "introspection.py", line 88, in wrapper_func
      return python_to_rpc(await result)
                           ^^^^^^^^^^^^
    File "/session/metadata/entry.py", line 5, in fetch
      res = await self.env.W1.add(1, 2)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "/lib/python3.13/site-packages/workers/_workers.py", line 1030, in wrapper
      return python_from_rpc(await result)
                             ^^^^^^^^^^^^
  pyodide.ffi.JsException: Error: Network connection lost.



[wrangler:info] GET / 500 Internal Server Error (73ms)
```
