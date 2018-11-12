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
  pspace;
  ImageLink;

  ngOnInit() {
      // this.backend.getlots().subscribe((data) => {
      //     this.lots = data;
      // });
  }

  setlabel(id){
      this.backend.getpspacenames(id).subscribe((data:pspacedata)=>{
          this.pspace = data.names;
          let urlCreator = window.URL;
        this.ImageLink = this.sanitizer.bypassSecurityTrustUrl(
            urlCreator.createObjectURL(data.image));
        document.getElementById("plotimage").style.display = 'block';
      })
  }

}
