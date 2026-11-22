// N9 rendering gate: same endpoint must move down when β increases, on fixed axes.
const { chromium } = require('playwright');
const path = require('path');
(async () => {
 const browser = await chromium.launch({headless:true, executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'});
 try {
  const page=await browser.newPage();
  await page.goto('file://'+path.resolve('index.html'));
  for(let i=0;i<8;i++) await page.locator('#next').click();
  async function sample(beta){
   await page.locator('#beta').fill(beta);
   return page.locator('#slope').evaluate(c=>{
    const ctx=c.getContext('2d');
    function center(x){const a=ctx.getImageData(x,15,1,c.height-65).data;let ys=[];for(let i=0;i<a.length;i+=4)if(a[i]>105&&a[i]<135&&a[i+1]>205&&a[i+1]<245&&a[i+2]>185&&a[i+2]<225)ys.push(15+i/4);return ys.length?ys.reduce((a,b)=>a+b)/ys.length:null;}
    return {left:center(106),right:center(c.width-30)};
   });
  }
  const shallow=await sample('0.2'),steep=await sample('2.4');
  const ok=Object.values(shallow).every(v=>v!==null)&&Object.values(steep).every(v=>v!==null)&&Math.abs(shallow.left-steep.left)<8&&steep.right-shallow.right>40;
  console.log(JSON.stringify({gate:'N9 fixed-axis exponent rendering',shallow,steep,result:ok?'PASS':'FAIL'},null,2));
  if(!ok)process.exitCode=1;
 } finally {await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1});
