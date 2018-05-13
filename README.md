# Signal Processing Wiener-Filter 

### Objectives
    • Wiener filter design
    • Signal estimation
    • Using signal models in signal prediction.
    • Documentation with Latex.

### Implementation
    Given a distorted ECG signal. We have modelled the distortion as  follow
    y(n) = cx(n) + v(n)
    where y(n) is the distorted signal. x(n) is the source signal, and v(n) is WGN v(n) ∼ N (0, σ2). c = −3
    and σ2 = 0.02
    • Using provided model, build a third order Wiener filter.
    • Apply this filter on the signal and show the  output.
    • Calculate mean square error of filtered signal (Source signal is provided for that).

### Report
    Report in a tex file Includes
    • Problem formulation
    • Implementation detail
    • Sample results



### Useful links

* Installing Latex for windows: Download and install [MikTex](https://miktex.org/download), then install [TexMaker](http://www.xm1math.net/texmaker/index.html).
* Installing Latex for Linux: follow [this](https://milq.github.io/install-latex-ubuntu-debian/)
* [Online](https://www.sharelatex.com/project) latex editor.
* Latex [tutorials](https://www.youtube.com/playlist?list=PLCRFsOKSM7ePUBOfh3O-K5XZldM5uCPwk)
