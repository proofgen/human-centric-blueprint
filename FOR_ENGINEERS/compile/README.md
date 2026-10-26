# The compiler

`compile.py` is the program that turned the text of this release into the data under `compiled/`. It is published so that you do not have to take the bundle on trust: run it on your copy of the text and compare what comes out with what was shipped.

    python3 FOR_ENGINEERS/compile/compile.py --tree . --out regenerated
    cat regenerated/bundle.sha256

Run from the top folder of the release. The second line must print the fingerprint in `README.md` and `compiled/bundle.sha256`. To see that every file matches, not only the fingerprint:

    diff -r regenerated compiled

One file under `compiled/` sits outside the seal and shows as present only on the shipped side: `verify.py`, the checker. Every other file is identical byte for byte, or the compiler has changed since the seal and the release does not match its text.

What this proves: the data was compiled from this text by this program, deterministically. What it does not prove: that the program reads the text correctly. For that, read the program. It is about two thousand lines of Python with no dependencies beyond the standard library, it holds no gate logic, and every place it stops the build is a place where the text and the data would otherwise have disagreed.

The release builder runs this same check at every build, so a release cannot ship unless its shipped compiler regenerates its shipped bundle.

Python 3.8 or later. Apache License 2.0 (the notice is at the top of the file); the text and the bundle are licensed as `LICENSE.md` states.
