from workers import WorkerEntrypoint, Response

class Default(WorkerEntrypoint):
    async def fetch(self, request):
        res = await self.env.W1.add(1, 2)
        return Response("OK")
