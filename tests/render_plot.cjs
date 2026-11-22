// N9 rendering gate: same endpoint must move down when β increases, on fixed axes.
const { chromium } = require('playwright');
const path = require('path');
(async () => {
 const browser = await chromium.launch({headless:true, executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'});
 try {
  const page=await browser.newPage();
  await page.goto('file://'+path.resolve('index.html'));
  for(let i=0;i<5;i++) await page.locator('#next').click();
  async function sample(beta){
   await page.locator('#beta').fill(beta);
   return page.locator('#slope').evaluate(c=>{
    const ctx=c.getContext('2d');
    function center(x){const a=ctx.getImageData(x,25,1,c.height-50).data;let ys=[];for(let i=0;i<a.length;i+=4)if(a[i]>90&&a[i]<155&&a[i+1]>170&&a[i+2]>160)ys.push(25+i/4);return ys.length?ys.reduce((a,b)=>a+b)/ys.length:null;}
    return {left:center(52),right:center(c.width-20)};
   });
  }
  const shallow=await sample('0.2'),steep=await sample('2.4');
  const ok=Object.values(shallow).every(v=>v!==null)&&Object.values(steep).every(v=>v!==null)&&Math.abs(shallow.left-steep.left)<8&&steep.right-shallow.right>40;
  console.log(JSON.stringify({gate:'N9 fixed-axis exponent rendering',shallow,steep,result:ok?'PASS':'FAIL'},null,2));
  if(!ok)process.exitCode=1;
 } finally {await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1});
