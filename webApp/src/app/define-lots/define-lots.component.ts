import { Component, OnInit } from '@angular/core';
import {PLot} from '../globals/plot';
import {Router} from '@angular/router';
import {BEService} from '../be.service';

@Component({
  selector: 'app-define-lots',
  templateUrl: './define-lots.component.html',
  styleUrls: ['./define-lots.component.css']
})
export class DefineLotsComponent implements OnInit {

  constructor(private backend: BEService, private router:Router) { }
  plots;
  sl = 0;
  baseURL = this.backend.baseURL;

  ngOnInit() {
      this.plots = [{'sl': 0,'name': 'test', 'lat': 25.3, 'long': 63.3, 'capacity': 23, 'image': null}];
  }

  addrow(){
    this.sl = this.sl + 1;
    this.plots.push({'sl': this.sl,'name': '', 'lat': 0, 'long': 0, 'capacity': 0, 'image': null});
  }

  onFileChanged(event, sl) {
    this.plots[sl].image = event.target.files[0];
    // var reader = new FileReader();
    // reader.onload =this._handleReaderLoaded.bind(this, sl);
    // reader.readAsBinaryString(event.target.files[0]);
  }
  _handleReaderLoaded(readerEvt, sl) {
       var binaryString = readerEvt.target.result;
              this.plots.b64= btoa(binaryString);
              console.log(btoa(binaryString));
      }

  finish(){
    // var form = document.getElementById("plotform");
    // var fdata = new FormData(form);
    console.log(this.plots);
      this.backend.post_define_lots(this.plots).subscribe((data) =>{
          console.log(data);
          this.router.navigateByUrl('/buildings');
      })
  }

}
