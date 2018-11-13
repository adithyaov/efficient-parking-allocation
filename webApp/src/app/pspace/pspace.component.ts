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
  lots;
  pspaces: any[];
  ImageLink;
  groups;

  ngOnInit() {
      this.backend.getlots().subscribe((data) => {
          this.lots = data;
      });
      this.backend.getgroups().subscribe((data)=>{
        this.groups = data;
      })
  }

  setlabel(id){
      this.pspaces = null;
      this.ImageLink = null;
      this.backend.getpspaceimage(id).subscribe((img)=>{
          let urlCreator = window.URL;
                // console.log(data)
              this.ImageLink = this.sanitizer.bypassSecurityTrustUrl(
                  urlCreator.createObjectURL(img));
          this.backend.getpspacenames(id).subscribe((data: any[]) => {
              this.pspaces = data;
              this.pspaces.forEach((p)=>{p.group = 0});
              document.getElementById("pspace-div").style.display = 'inline-block';
          })
      })
  }

  finish(){
      this.backend.postpspacenames(this.pspaces).subscribe((data)=>{
          console.log(data);
          alert('Updated :-)');
      });
  }

  finish_setup(){
      this.router.navigateByUrl('/');
  }

}
