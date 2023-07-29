#!/usr/bin/env python
import sys
import gogrepoc.gogrepoc as gogrepo

if __name__ == "__main__":
    try:
        wakelock = gogrepo.Wakelock()
        wakelock.take_wakelock()
        gogrepo.main(gogrepo.process_argv(sys.argv + ["update", "-os", "windows", "linux", "mac", "-lang", "en", "de"]))
        gogrepo.main(gogrepo.process_argv(sys.argv + ["download", "./Games", "-os", "windows", "linux", "mac", "-lang", "en", "de"]))
        gogrepo.main(gogrepo.process_argv(sys.argv + ["verify", "./Games"]))
        gogrepo.info('exiting...')
    except SystemExit:
        raise
    except Exception:
        gogrepo.log_exception('fatal...')
        sys.exit(1)
    finally:
        wakelock.release_wakelock()

