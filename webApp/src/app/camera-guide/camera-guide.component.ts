import { Component, OnInit } from '@angular/core';
import {Router} from '@angular/router';
import {BEService} from '../be.service';
import { DomSanitizer, SafeUrl } from '@angular/platform-browser';

@Component({
  selector: 'app-camera-guide',
  templateUrl: './camera-guide.component.html',
  styleUrls: ['./camera-guide.component.css']
})
export class CameraGuideComponent implements OnInit {

  constructor(private backend:BEService, private router:Router, private sanitizer: DomSanitizer) { }
  image;
  scale;
  ImageLink;

  ngOnInit() {
  }

  onFileChanged(event) {
    this.image = event.target.files[0];
  }

  finish(){
      this.backend.getcameraguide(this.image, this.scale).subscribe((data) => {
          let urlCreator = window.URL;
        this.ImageLink = this.sanitizer.bypassSecurityTrustUrl(
            urlCreator.createObjectURL(data));
        document.getElementById("responseimage").style.display = 'block';
      });
  }

}
