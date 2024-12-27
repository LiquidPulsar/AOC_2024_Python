from contextlib import redirect_stderr, redirect_stdout
from importlib import import_module
from time import perf_counter

LIM = 25

class NullStream:
    def write(self, *args, **kwargs):
        pass

    def flush(self):
        pass

if __name__ == "__main__":
    total = 0
    times = []
    for n in range(1, LIM + 1):
        for p in range(2, 3):
            with redirect_stdout(None), redirect_stderr(NullStream()): # type: ignore
                t = perf_counter()
                if n in (6, 22) and p == 2:
                    import_module(f"Day_{n}.p{p}").main()
                import_module(f"Day_{n}.p{p}")
            print(f"Day {n:02d} Part {p}: {(dt := perf_counter() - t):.7f}s{'!!!'*int(dt / 0.2)}")
            total += dt
            times.append(dt)

    print("Total:", total)
    print("Max:", max(times))
    print("Min:", min(times))
    print("Avg:", total / len(times))
    top = sorted(times, reverse=True)[:8]
    print(
        f"Top 8: {top} account for {sum(top)}s ({sum(top) / total:.2%}% of total)"
    )
