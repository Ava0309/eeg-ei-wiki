const assert=require('assert');
const m=require('../slides/interactions.js');
const near=(a,b,e=1e-8)=>assert(Math.abs(a-b)<e,`${a} != ${b}`);
const fs=128,N=128;let x=Array.from({length:N},(_,i)=>Math.sin(2*Math.PI*4*i/fs)+.5*Math.sin(2*Math.PI*10*i/fs));
near(m.amplitude(x,4),1);near(m.amplitude(x,10),.5);near(m.amplitude(x,7),0);
for(let n=0;n<12;n++)near(Math.sin(2*Math.PI*10*n/12),-Math.sin(2*Math.PI*2*n/12));
let tone=Array.from({length:512},(_,i)=>.8*Math.sin(2*Math.PI*10*i/fs));let w=m.welch(tone,fs,128,64);assert.equal(w.count,7);assert.equal(w.average.indexOf(Math.max(...w.average)),10);near(w.average.reduce((a,b)=>a+b,0),.32,.0001);
let s=m.syntheticSignal(),a=m.welch(s,128,128,64),scaled=m.welch(s.map(v=>2*v),128,128,64);a.average.forEach((v,i)=>near(scaled.average[i],4*v,1e-9));
let low=m.decomposition(.5),high=m.decomposition(1.5);assert(low.band>high.band);near(low.peak[45],high.peak[45]);
console.log('PASS: DFT amplitude, sampling alias, Welch 7 windows / PSD normalization and scaling, decomposition band effect');
// N8 follow-up: signed DFT frequency mapping and reference-normalized power-law examples.
const signedFrequency=(k,N,fs)=>k<=N/2?k*fs/N:(k-N)*fs/N;
near(signedFrequency(10,128,128),10);near(signedFrequency(118,128,128),-10);
const normalizedPower=(f,f0,p0,beta)=>p0*Math.pow(f/f0,-beta);
near(normalizedPower(10,1,1,1),.1);near(normalizedPower(10,1,1,2),.01);
near(Math.log10(normalizedPower(10,1,1,2)/1),-2*Math.log10(10/1));
console.log('PASS: signed DFT frequency mapping and dimensionless reference-normalized exponent example');
