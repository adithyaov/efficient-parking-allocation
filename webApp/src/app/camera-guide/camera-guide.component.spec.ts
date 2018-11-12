import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CameraGuideComponent } from './camera-guide.component';

describe('CameraGuideComponent', () => {
  let component: CameraGuideComponent;
  let fixture: ComponentFixture<CameraGuideComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CameraGuideComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CameraGuideComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
