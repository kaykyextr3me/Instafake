
    var crl = document.getElementById('myCrl').getContext('2d');

    crl.beginPath();
    crl.arc(60, 100, 40, 0, 2 * Math.PI);
    crl.fillStyle = '#00ACC1';
    crl.fill();
    crl.linewidth = 5;
    crl.strokeStyle = '#dbdbdb';
    crl.stroke();

    var crl1 = document.getElementById('myCrl1').getContext('2d');

    crl1.beginPath();
    crl1.arc(60, 100, 40, 0, 2 * Math.PI);
    crl1.fillStyle = '#F8BBD0';
    crl1.fill();
    crl1.linewidth = 5;
    crl1.strokeStyle = '#dbdbdb';
    crl1.stroke();

    var crl2 = document.getElementById('myCrl2').getContext('2d');

    crl2.beginPath();
    crl2.arc(60, 100, 40, 0, 2 * Math.PI);
    crl2.fillStyle = '#E91E63';
    crl2.fill();
    crl2.linewidth = 5;
    crl2.strokeStyle = '#dbdbdb';
    crl2.stroke();

    const popupCenter = ({url, title, w, h}) => {
    // Fixes dual-screen position                             Most browsers      Firefox
    const dualScreenLeft = window.screenLeft !==  undefined ? window.screenLeft : window.screenX;
    const dualScreenTop = window.screenTop !==  undefined   ? window.screenTop  : window.screenY;

    const width = window.innerWidth ? window.innerWidth : document.documentElement.clientWidth ? document.documentElement.clientWidth : screen.width;
    const height = window.innerHeight ? window.innerHeight : document.documentElement.clientHeight ? document.documentElement.clientHeight : screen.height;

    const systemZoom = width / window.screen.availWidth;
    const left = (width - w) / 2 / systemZoom + dualScreenLeft
    const top = (height - h) / 2 / systemZoom + dualScreenTop
    const newWindow = window.open(url, title, 
      `
      scrollbars=yes,
      width=${w / systemZoom}, 
      height=${h / systemZoom}, 
      top=${top}, 
      left=${left}
      `
    )

    if (window.focus) newWindow.focus();
}


