@import url('../assets/site.css');

body {
    padding: 120px max(20px, calc((100vw - 1000px) / 2));
}

.back {
    color: #9eb2ca;
    font-size: 13px;
}

.page-head {
    margin: 70px 0 50px;
}

.page-head h1 {
    font-size: clamp(52px, 8vw, 96px);
    letter-spacing: -0.065em;
    line-height: 0.95;
    margin: 12px 0;
}

.page-head p {
    color: var(--muted);
    max-width: 700px;
    font-size: 18px;
}

.content {
    border-top: 1px solid var(--line);
    padding-top: 35px;
}

.content h2 {
    font-size: 28px;
}

.content p,
.content li {
    color: #aab5c4;
}

.pub {
    padding: 22px 0;
    border-bottom: 1px solid var(--line);
}
