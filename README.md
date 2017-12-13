# SVN-Conflict-Manager
[SVN Conflict Manager] When multiple process try to update the same local copy of SVN ,it causes the conflict and leads to locking of the local copy .SVN Conflict Manager will handle this situation in such a way that ,it will keep the SVN update request in a queue and then it will let them complete there task without locking the local SVN workspace.

Requirments: 
  Python
  
Input:
  Directory path for SVN local copy.
  
Funcitionality:
  1. It will check Input path is correct or not.
  2. It will cheeck Input path is under Subversion or not.
  3. Any other parallel task will be monitored.
  4. Most kinds of errrors are handled.
  5. It prevents the major conflicts while updating workspace.
  
 
