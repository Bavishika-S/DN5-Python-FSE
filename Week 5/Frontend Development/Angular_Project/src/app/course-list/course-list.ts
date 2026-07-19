import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-course-list',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './course-list.html',
  styleUrl: './course-list.css'
})
export class CourseListComponent {

  courses = [
    { name: 'Web Development', credits: 4 },
    { name: 'React', credits: 4 },
    { name: 'Angular', credits: 3 },
    { name: 'Vue', credits: 3 },
    { name: 'Python', credits: 4 }
  ];

}