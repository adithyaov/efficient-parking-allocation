import { Component, OnInit } from '@angular/core';
import {Router} from '@angular/router';
import {BEService} from '../be.service';
import { DomSanitizer, SafeUrl } from '@angular/platform-browser';

@Component({
  selector: 'app-pspace',
  templateUrl: './pspace.component.html',
  styleUrls: ['./pspace.component.css']
})
export class PSpaceComponent implements OnInit {

  constructor(private backend: BEService, private router:Router, private sanitizer: DomSanitizer) { }
  lots = [{'name': 'asd', 'id':2}];
  pspaces;
  ImageLink;

  ngOnInit() {
      // this.backend.getlots().subscribe((data) => {
      //     this.lots = data;
      // });
  }

  setlabel(id){
      this.pspaces = null;
      this.ImageLink = null;
      this.backend.getpspacenames(id).subscribe((data)=>{
          this.pspaces = data;
          this.backend.getpspaceimage(id).subscribe((img) => {
                let urlCreator = window.URL;
                console.log(data)
              this.ImageLink = this.sanitizer.bypassSecurityTrustUrl(
                  urlCreator.createObjectURL(img));
              document.getElementById("pspace-div").style.display = 'block';
          })
      })
  }

  finish(){
      this.backend.postpspacenames(this.pspaces).subscribe((data)=>{
          console.log(data);
      });
  }

}
