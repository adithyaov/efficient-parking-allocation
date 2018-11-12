import { Component, OnInit } from '@angular/core';
import {Router} from '@angular/router';
import {BEService} from '../be.service';
import { DomSanitizer, SafeUrl } from '@angular/platform-browser';

interface pspacedata{
    image:any;
    names:any;
}
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
      this.backend.getpspacenames(id).subscribe((data:pspacedata)=>{
          this.pspaces = data.names;
          let urlCreator = window.URL;
        this.ImageLink = this.sanitizer.bypassSecurityTrustUrl(
            urlCreator.createObjectURL(data.image));
        document.getElementById("pspace-div").style.display = 'block';
      })
  }

  finish(){
      this.backend.postpspacenames(this.pspaces).subscribe((data)=>{
          console.log(data);
      });
  }

}
